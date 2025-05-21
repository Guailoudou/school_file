<template>
  <div class="practice-section">
    <h2 class="main-title">练习区域</h2>

    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>练习概述</h4>
      <div class="intro-content">
        <p>本练习区域提供了一系列与示例区域对应的实践任务，帮助您巩固所学的Vue 3高级特性。</p>
        <p>请尝试实现动态组件切换、插槽内容分发以及自定义指令功能，将理论知识转化为实际编码能力。</p>
        <p>每个练习都提供了明确的任务目标和基础代码结构，您需要完成剩余的实现部分。</p>
      </div>
    </section>

    <!-- 动态组件和 KeepAlive -->
    <div class="experiment-section">
      <h3>1. 动态组件与 KeepAlive 练习</h3>
      <div class="experiment-desc">本练习要求您实现组件的动态切换和状态保持功能。完成后，您将能够使用按钮在不同组件间切换，并保持某些组件的状态，体验KeepAlive的实际应用效果。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>创建两个简单组件 (例如 ComponentA, ComponentB)。</li>
            <li>使用按钮切换动态显示这两个组件。</li>
            <li>使用 <code>&lt;KeepAlive&gt;</code> 缓存其中一个组件的状态。</li>
          </ul>
        </div>
        <!-- 动态组件练习区域 -->
        <div class="practice-area">
          <div class="controls">
            <button>显示组件 A</button>
            <button>显示组件 B</button>
            <button>显示组件 C</button>
          </div>
          <div class="dynamic-component-container">
            <!-- <KeepAlive :include="['ComponentBPractice', 'ComponentCPractice']">
              <component :is="currentComponent"></component>
            </KeepAlive> -->
            <p class="placeholder-text">在此处放置动态组件</p>
          </div>
          <p class="component-explanation">
            提示：使用shallowRef创建组件引用，通过点击事件更新currentComponent变量，使用KeepAlive包裹component元素。
          </p>
        </div>
      </div>
    </div>

    <!-- 插槽 -->
    <div class="experiment-section">
      <h3>2. 插槽 (Slots) 练习</h3>
      <div class="experiment-desc">本练习要求您实现三种不同类型的插槽。完成后，您将掌握如何使用默认插槽、具名插槽和作用域插槽，理解Vue组件内容分发的灵活性和强大功能。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>创建一个带默认插槽的组件 (例如 BaseLayout)。</li>
            <li>创建一个带具名插槽的组件 (例如 Card)，包含 header 和 footer 插槽。</li>
            <li>创建一个带作用域插槽的组件 (例如 ItemList)，向父组件传递列表项数据。</li>
          </ul>
        </div>
        <!-- 插槽练习区域 -->
        <div class="practice-area">
          <h4>默认插槽示例</h4>
          <div class="slot-demo">
            <!-- 学生需要在此处使用 BaseLayoutPractice 组件并填充默认插槽 -->
            <p class="placeholder-text">在此处使用带默认插槽的组件</p>
            <p class="slot-explanation">提示：导入BaseLayoutPractice组件，组件内部应包含&lt;slot&gt;标签</p>
          </div>

          <h4>具名插槽示例</h4>
          <div class="slot-demo">
            <!-- 学生需要在此处使用 CardPractice 组件并填充 header, default, footer 插槽 -->
            <p class="placeholder-text">在此处使用带具名插槽的组件</p>
            <p class="slot-explanation">提示：导入CardPractice组件，组件内部应包含&lt;slot name="header"&gt;、&lt;slot&gt;和&lt;slot
              name="footer"&gt;标签</p>
          </div>

          <h4>作用域插槽示例</h4>
          <div class="slot-demo">
            <!-- 学生需要在此处使用 ItemListPractice 组件并接收作用域插槽数据 -->
            <p class="placeholder-text">在此处使用带作用域插槽的组件</p>
            <p class="slot-explanation">提示：导入ItemListPractice组件，组件内部应包含&lt;slot :item="item" :index="index"&gt;传递数据</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 自定义指令 -->
    <div class="experiment-section">
      <h3>3. 自定义指令 (Custom Directives) 练习</h3>
      <div class="experiment-desc">本练习要求您实现自定义指令功能。完成后，您将掌握如何创建和使用Vue自定义指令，直接操作DOM元素，实现特殊的交互效果和功能扩展。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>创建一个私有自定义指令 (例如 v-highlight)，用于高亮显示元素的背景色。</li>
            <li>将该指令应用到一个 DOM 元素上。</li>
          </ul>
        </div>
        <!-- 自定义指令练习区域 -->
        <div class="practice-area">
          <div class="directive-demo">
            <h4>高亮指令实现</h4>
            <div class="color-buttons">
              <button @click="highlightColor = '#ffff99'" :class="{ active: highlightColor === '#ffff99' }">黄色</button>
              <button @click="highlightColor = '#90ee90'" :class="{ active: highlightColor === '#90ee90' }">浅绿色</button>
              <button @click="highlightColor = '#add8e6'" :class="{ active: highlightColor === '#add8e6' }">浅蓝色</button>
              <button @click="highlightColor = '#ffc0cb'" :class="{ active: highlightColor === '#ffc0cb' }">粉色</button>
            </div>
            <p class="highlight-text" >应用v-highlight指令到这段文字上</p>
            <p class="directive-explanation">提示：定义vHighlight指令对象，包含mounted和updated钩子函数，在函数内修改元素的背景色</p>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 学生需要在此处导入所需组件和函数
// import { ref, shallowRef } from 'vue'
// import ComponentAPractice from './experiment3/ComponentAPractice.vue'
// import ComponentBPractice from './experiment3/ComponentBPractice.vue'
// import ComponentCPractice from './experiment3/ComponentCPractice.vue'
// import BaseLayoutPractice from './experiment3/BaseLayoutPractice.vue'
// import CardPractice from './experiment3/CardPractice.vue'
// import ItemListPractice from './experiment3/ItemListPractice.vue'

// 动态组件练习：学生需要定义 currentComponent 和切换逻辑
// const ComponentA = shallowRef(ComponentAPractice)
// const ComponentB = shallowRef(ComponentBPractice)
// const ComponentC = shallowRef(ComponentCPractice)
// const currentComponent = shallowRef(ComponentA)

// 自定义指令相关变量
const highlightColor = ref('#ffff99') // 默认黄色

// 自定义指令：v-highlight
const vHighlight = {
  mounted(el, binding) {
    
  },
  updated(el, binding) {
    
  }
}

</script>

<style scoped>
/* 沿用实验二的样式 */
.practice-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  height: 100%;
  overflow-y: auto;
}

/* 实验介绍样式 */
.experiment-introduction {
  margin: 0.5rem 0 1.5rem 0;
  padding: 1rem 1.2rem;
  background-color: #f0f7f4;
  border-left: 4px solid #42b983;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experiment-introduction:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(66, 185, 131, 0.1);
}

.experiment-introduction h4 {
  color: #2c3e50;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.intro-content p {
  margin: 0.6rem 0;
  line-height: 1.6;
  color: #34495e;
}

/* 实验描述样式 */
.experiment-desc {
  margin: 0.5rem 0 1rem 0;
  padding: 0.8rem 1rem;
  background-color: #edf7f2;
  border-radius: 6px;
  color: #3c6357;
  font-size: 0.95rem;
  line-height: 1.5;
  border-left: 3px solid #42b983;
}

.main-title {
  color: #2c3e50;
  font-size: 1.8rem;
  text-align: center;
  margin-bottom: 2rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.main-title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #42b983, #2f9c69);
  border-radius: 2px;
}

.experiment-section {
  margin-bottom: 2.5rem;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  overflow: hidden;
}

.experiment-section h3 {
  background: #f8f8f8;
  color: #2c3e50;
  margin: 0;
  padding: 1rem;
  font-size: 1.4rem;
  border-bottom: 1px solid #e8e8e8;
}

.content-box {
  padding: 1.5rem;
}

.description {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: #f8f8f8;
  border-radius: 6px;
  border-left: 4px solid #42b983;
}

.description p {
  margin: 0 0 0.5rem 0;
  color: #666;
  font-size: 0.9rem;
}

.description ul {
  margin: 0;
  padding-left: 1.2rem;
  color: #666;
  font-size: 0.9rem;
}

.description li {
  margin: 0.3rem 0;
}

.practice-area {
  margin-top: 1.5rem;
  padding: 1rem;
  border: 1px solid #eaeaea;
  border-radius: 6px;
  background-color: #fafafa;
}

.controls {
  margin-bottom: 1rem;
}

.controls button {
  margin-right: 10px;
  padding: 6px 12px;
  background: linear-gradient(to bottom, #42b983, #3aa876);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.controls button:hover {
  background: linear-gradient(to bottom, #3aa876, #2f9c69);
  transform: translateY(-2px);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.scoped-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px;
  border-radius: 4px;
  background-color: #f5f5f5;
  margin-bottom: 8px;
}

.scoped-item button {
  padding: 3px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[placeholder] {
  padding: 8px;
  width: 100%;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin: 10px 0;
}

/* 动态组件容器样式 */
.dynamic-component-container {
  margin: 1rem 0;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #f9f9f9;
  min-height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 组件说明样式 */
.component-explanation {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #666;
  font-style: italic;
  padding: 0.5rem;
  background-color: #f5f5f5;
  border-radius: 4px;
}

/* 插槽演示区域样式 */
.slot-demo {
  margin: 1rem 0 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px dashed #eee;
}

.slot-explanation {
  margin-top: 0.8rem;
  font-size: 0.85rem;
  color: #666;
  font-style: italic;
  padding-left: 0.5rem;
  border-left: 2px solid #42b983;
}

/* 自定义指令演示区域样式 */
.directive-demo {
  margin: 1rem 0 2rem;
  padding: 1.2rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e7e7e7;
}

.directive-explanation {
  margin-top: 0.8rem;
  font-size: 0.85rem;
  color: #666;
  font-style: italic;
  padding-left: 0.5rem;
  border-left: 2px solid #42b983;
}

.highlight-text {
  padding: 1rem;
  border-radius: 6px;
  transition: background-color 0.3s ease;
  margin: 1rem 0;
  font-size: 1.1rem;
}

.color-buttons {
  display: flex;
  gap: 0.5rem;
  margin: 0.5rem 0 1rem;
}

.color-buttons button {
  padding: 0.4rem 1rem;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.color-buttons button:hover {
  transform: translateY(-2px);
}

.color-buttons button.active {
  border-color: #42b983;
  background-color: rgba(66, 185, 131, 0.1);
  box-shadow: 0 0 0 1px #42b983;
}

.focus-demo {
  display: flex;
  gap: 0.8rem;
  margin: 1rem 0;
  align-items: center;
}

.focus-demo input {
  flex: 1;
}

/* 占位符文字样式 */
.placeholder-text {
  color: #999;
  border: 1px dashed #ccc;
  padding: 1rem;
  text-align: center;
  background-color: #f7f7f7;
  font-style: italic;
}

@media (max-width: 768px) {
  .practice-section {
    padding: 1rem;
  }

  .experiment-section h3 {
    font-size: 1.2rem;
  }
}
</style>