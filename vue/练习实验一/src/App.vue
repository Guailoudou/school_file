<script setup>
import { ref } from 'vue'

const experiments = ref([
  { name: '实验1：数据绑定', path: '/experiment1' }
])
</script>

<template>
  <div class="app">
    <aside class="sidebar">
      <div class="sidebar-header">
        <h1>Vue.js 学习实验</h1>
      </div>
      <nav class="nav-menu">
        <router-link 
          v-for="(exp, index) in experiments" 
          :key="index"
          :to="exp.path"
          class="nav-link"
          active-class="active"
        >
          {{ exp.name }}
        </router-link>
      </nav>
    </aside>

    <div class="main-container">
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

/* 侧边栏样式 */
.sidebar {
  width: 280px;
  background: linear-gradient(135deg, #42b983 0%, #33a06f 100%);
  color: white;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  height: 100vh;
  left: 0;
  top: 0;
}

.sidebar-header {
  padding: 2rem 1.5rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-header h1 {
  font-size: 1.5rem;
  font-weight: 600;
}

/* 导航菜单样式 */
.nav-menu {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 0;
  gap: 0.5rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  transition: all 0.3s ease;
  opacity: 0.8;
  border-left: 4px solid transparent;
}

.nav-link:hover {
  opacity: 1;
  background-color: rgba(255, 255, 255, 0.1);
  border-left-color: white;
}

.nav-link.active {
  opacity: 1;
  background-color: rgba(255, 255, 255, 0.15);
  border-left-color: white;
  font-weight: 600;
}

/* 主容器样式 */
.main-container {
  flex: 1;
  margin-left: 280px;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
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
    width: 100%;
    height: auto;
    position: relative;
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

  .nav-link:hover,
  .nav-link.active {
    border-left: none;
    background-color: rgba(255, 255, 255, 0.2);
  }

  .main-container {
    margin-left: 0;
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
