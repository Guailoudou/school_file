<script setup>
import { ref } from 'vue'

const experiments = ref([
  { name: '实验2：组件通信', path: '/experiment2' },
  { name: '实验3：动态组件', path: '/experiment3' },
])

// 侧边栏宽度相关变量和方法
const sidebarWidth = ref(280) // 默认宽度
const isDragging = ref(false)
const minWidth = 200 // 最小宽度
const maxWidth = 500 // 最大宽度
const isCollapsed = ref(false) // 折叠状态
const collapsedWidth = 60 // 折叠时的宽度

// 开始拖动
const startDrag = (e) => {
  if (!isCollapsed.value) {
    isDragging.value = true
    document.addEventListener('mousemove', onDrag)
    document.addEventListener('mouseup', stopDrag)
    e.preventDefault() // 防止选中文本
  }
}

// 拖动中
const onDrag = (e) => {
  if (isDragging.value) {
    let newWidth = e.clientX
    // 限制最小和最大宽度
    if (newWidth < minWidth) newWidth = minWidth
    if (newWidth > maxWidth) newWidth = maxWidth
    sidebarWidth.value = newWidth
  }
}

// 停止拖动
const stopDrag = () => {
  isDragging.value = false
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
}

// 切换折叠状态
const toggleCollapse = () => {
  isCollapsed.value = !isCollapsed.value
}
</script>

<template>
  <div class="app" :class="{ 'dragging': isDragging }">
    <aside class="sidebar" :style="{ width: isCollapsed ? collapsedWidth + 'px' : sidebarWidth + 'px' }" :class="{ 'collapsed': isCollapsed }">
      <div class="sidebar-header">
        <h1 v-show="!isCollapsed">Vue.js 学习实验</h1>
      </div>
      
      <!-- 切换折叠按钮 -->
      <button class="collapse-toggle" @click="toggleCollapse">
        <span v-if="isCollapsed">&#9654;</span> <!-- 右箭头 -->
        <span v-else>&#9664;</span> <!-- 左箭头 -->
      </button>
      
      <nav class="nav-menu">
        <router-link 
          v-for="(exp, index) in experiments" 
          :key="index"
          :to="exp.path"
          class="nav-link"
          active-class="active"
          :title="exp.name"
        >
          <span class="nav-icon">{{ exp.name.charAt(2) }}</span> <!-- 使用实验编号作为图标 -->
          <span class="nav-text" v-show="!isCollapsed">{{ exp.name }}</span>
        </router-link>
      </nav>
    </aside>

    <!-- 宽度调整把手 -->
    <div 
      class="resize-handle" 
      @mousedown="startDrag"
      :style="{ marginLeft: isCollapsed ? collapsedWidth + 'px' : sidebarWidth + 'px' }"
      v-show="!isCollapsed"
    ></div>

    <div class="main-container" :style="{ marginLeft: isCollapsed ? collapsedWidth + 'px' : sidebarWidth + 'px' }">
      <main class="app-main">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>

      <footer class="app-footer">
        <p>Vue.js 学习项目 - 实验练习</p>
      </footer>
    </div>
  </div>
</template>

<style>
/* 全局样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  color: #2c3e50;
  background-color: #f5f7fa;
}

/* 应用容器样式 */
.app {
  min-height: 100vh;
  display: flex;
}

/* 当正在拖动时添加这个类，防止文本选择 */
.app.dragging {
  user-select: none;
  cursor: col-resize;
}

/* 侧边栏样式 */
.sidebar {
  background: linear-gradient(135deg, #42b983 0%, #33a06f 100%);
  color: white;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  height: 100vh;
  left: 0;
  top: 0;
  overflow-x: hidden; /* 防止内容溢出 */
  transition: width 0.3s ease-out; /* 添加平滑过渡效果 */
  z-index: 10;
}

/* 折叠按钮样式 */
.collapse-toggle {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s;
  z-index: 15;
}

.collapse-toggle:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.sidebar.collapsed .collapse-toggle {
  left: 18px; /* 居中放置在折叠栏中 */
  right: auto;
}

/* 宽度调整把手 */
.resize-handle {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  width: 6px; /* 宽度调整把手的宽度 */
  background-color: transparent;
  cursor: col-resize;
  z-index: 100;
  transition: margin-left 0.3s ease-out;
}

.resize-handle:hover, 
.resize-handle:active {
  background-color: rgba(0, 0, 0, 0.1);
}

.sidebar-header {
  padding: 2rem 1.5rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar.collapsed .sidebar-header {
  padding: 0.5rem;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.sidebar-header h1 {
  font-size: 1.5rem;
  font-weight: 600;
  white-space: nowrap; /* 防止文本换行 */
  overflow: hidden;
  text-overflow: ellipsis; /* 文本溢出时显示省略号 */
}

/* 导航菜单样式 */
.nav-menu {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 0;
  gap: 0.5rem;
  overflow-y: auto; /* 如果菜单项过多，允许滚动 */
}

.sidebar.collapsed .nav-menu {
  padding: 0.5rem 0;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  transition: all 0.3s ease;
  opacity: 0.8;
  border-left: 4px solid transparent;
  white-space: nowrap; /* 防止文本换行 */
  overflow: hidden;
  text-overflow: ellipsis; /* 文本溢出时显示省略号 */
  display: flex;
  align-items: center;
}

.nav-icon {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 28px;
  height: 28px;
  margin-right: 10px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.15);
  font-weight: bold;
}

.sidebar.collapsed .nav-link {
  justify-content: center;
  padding: 0.8rem 0;
  width: 100%;
  border-left: none;
}

.sidebar.collapsed .nav-icon {
  margin-right: 0;
}

.nav-link:hover {
  opacity: 1;
  background-color: rgba(255, 255, 255, 0.1);
  border-left-color: white;
}

.sidebar.collapsed .nav-link:hover {
  border-left: none;
  background-color: rgba(255, 255, 255, 0.15);
}

.nav-link.active {
  opacity: 1;
  background-color: rgba(255, 255, 255, 0.15);
  border-left-color: white;
  font-weight: 600;
}

.sidebar.collapsed .nav-link.active {
  border-left: none;
}

.sidebar.collapsed .nav-link.active .nav-icon {
  background-color: rgba(255, 255, 255, 0.3);
}

/* 主容器样式 */
.main-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: margin-left 0.3s ease-out; /* 添加平滑过渡效果 */
}

/* 主要内容区域样式 */
.app-main {
  flex: 1;
  padding: 2rem;
  max-width: 1600px;
  margin: 0 auto;
  width: 100%;
}

/* 页脚样式 */
.app-footer {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}

/* 过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 响应式设计 */
@media (max-width: 1600px) {
  .app-main {
    max-width: 1400px;
    padding: 1.8rem;
  }
}

@media (max-width: 1440px) {
  .app-main {
    max-width: 1200px;
    padding: 1.5rem;
  }
}

@media (max-width: 1200px) {
  .app-main {
    max-width: 1000px;
    padding: 1.2rem;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 100% !important; /* 强制覆盖行内样式 */
    height: auto;
    position: relative;
  }
  
  .resize-handle {
    display: none; /* 在移动设备上隐藏调整把手 */
  }
  
  .collapse-toggle {
    display: none; /* 在移动设备上隐藏折叠按钮 */
  }

  .sidebar-header {
    padding: 1rem;
  }

  .nav-menu {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    padding: 0.5rem;
    gap: 0.5rem;
  }

  .nav-link {
    padding: 0.5rem 1rem;
    border-left: none;
    border-radius: 20px;
  }
  
  .nav-icon {
    display: none;
  }

  .nav-link:hover,
  .nav-link.active {
    border-left: none;
    background-color: rgba(255, 255, 255, 0.2);
  }

  .main-container {
    margin-left: 0 !important; /* 强制覆盖行内样式 */
  }

  .app-main {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .sidebar-header h1 {
    font-size: 1.2rem;
  }

  .nav-link {
    font-size: 0.9rem;
    padding: 0.4rem 0.8rem;
  }

  .app-main {
    padding: 0.8rem;
  }
}
</style>
