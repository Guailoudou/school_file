<template>
  <div class="example-section">
    <h2 class="main-title">示例区域</h2>
    
    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>实验概述</h4>
      <div class="intro-content">
        <p>本实验展示了Vue 3中的高级特性，包括动态组件、插槽系统和自定义指令的实现和应用。</p>
        <p>通过这些示例，您将学习如何动态切换组件、使用不同类型的插槽进行内容分发，以及创建自定义指令扩展Vue的功能。</p>
        <p>每个示例都提供了可交互的演示，您可以直接操作体验这些高级特性的效果。</p>
      </div>
    </section>
    
    <!-- 动态组件和 KeepAlive -->
    <div class="experiment-section">
      <h3>1. 动态组件与 KeepAlive</h3>
      <div class="experiment-desc">本实验演示了组件的动态切换和状态保持。点击不同按钮可以在三个组件之间切换，KeepAlive包装器使组件B和C的状态在切换后仍然保持，而组件A每次都会重新创建。</div>
      <div class="content-box">
        <div class="description">
          <p>使用 <code>&lt;component :is="..."&gt;</code> 实现动态组件渲染，并用 <code>&lt;KeepAlive&gt;</code> 缓存组件状态。</p>
        </div>
        <!-- 切换按钮区域 -->
        <div class="controls">
          <button @click="currentComponent = ComponentA">显示组件 A</button>
          <button @click="currentComponent = ComponentB">显示组件 B</button>
          <button @click="currentComponent = ComponentC">显示组件 C</button>
        </div>
        <!-- 动态组件展示区域 -->
        <!-- KeepAlive只包含ComponentB和C，A组件每次都会重新创建 -->
        <div class="dynamic-component-container">
          <KeepAlive :include="['ComponentBExample', 'ComponentCExample']">
            <component :is="currentComponent"></component>
          </KeepAlive>
        </div>
        <!-- 动态组件说明 -->
        <p class="component-explanation">
          尝试在组件B或C中输入内容，然后切换到其他组件后再切回，观察状态是否保留。
          组件A不在include列表中，所以每次切换回A时都会重新创建。
        </p>
      </div>
    </div>

    <!-- 插槽 -->
    <div class="experiment-section">
      <h3>2. 插槽 (Slots)</h3>
      <div class="experiment-desc">本实验展示了三种插槽的使用方式。默认插槽接收简单内容；具名插槽通过名称将内容分发到组件的不同位置；作用域插槽则能访问子组件内部的数据并在父组件中使用。</div>
      <div class="content-box">
        <div class="description">
          <p>演示默认插槽、具名插槽和作用域插槽的用法。</p>
        </div>
        
        <!-- 默认插槽示例 -->
        <h4>默认插槽示例</h4>
        <div class="slot-demo">
          <!-- 向BaseLayout组件的默认插槽传递内容 -->
          <BaseLayoutExample>
            <p>这是插入到 BaseLayout 默认插槽的内容。</p>
          </BaseLayoutExample>
          <p class="slot-explanation">原理：组件内使用&lt;slot&gt;标签定义插槽位置，父组件可以将任意内容传入该位置。</p>
        </div>

        <!-- 具名插槽示例 -->
        <h4>具名插槽示例</h4>
        <div class="slot-demo">
          <!-- 使用template和#语法向特定名称的插槽传递内容 -->
          <CardExample>
            <!-- #header是v-slot:header的简写 -->
            <template #header>
              <h3>自定义卡片标题</h3>
            </template>
            <template #default>
              <p>这是卡片的主要内容区域。</p>
            </template>
            <template #footer>
              <span>自定义底部信息 - {{ new Date().toLocaleTimeString() }}</span>
            </template>
          </CardExample>
          <p class="slot-explanation">原理：组件内使用&lt;slot name="xxx"&gt;定义多个具名插槽，父组件使用template和v-slot:xxx或#xxx语法指定内容应该放在哪个插槽中。</p>
        </div>

        <!-- 作用域插槽示例 -->
        <h4>作用域插槽示例</h4>
        <div class="slot-demo">
          <!-- v-slot="{ item, index }"接收子组件传递的数据 -->
          <ItemListExample v-slot="{ item, index }">
            <div class="scoped-item">
              <span>序号 {{ index + 1 }}: {{ item.text }}</span>
              <button>操作</button>
            </div>
          </ItemListExample>
          <p class="slot-explanation">原理：子组件通过&lt;slot :item="..."&gt;向插槽传递数据，父组件使用v-slot="{ item }"接收并使用这些数据。</p>
        </div>
      </div>
    </div>

    <!-- 自定义指令 -->
    <div class="experiment-section">
      <h3>3. 自定义指令 (Custom Directives)</h3>
      <div class="experiment-desc">本实验演示了如何创建和使用自定义指令。自定义指令可以直接操作DOM元素，为Vue组件添加底层功能。下方展示了多种自定义指令的应用场景，您可以尝试不同交互来体验效果。</div>
      <div class="content-box">
        <div class="description">
          <p>演示如何创建和使用多种自定义指令，实现特殊的DOM交互效果。</p>
        </div>
        
        <!-- 高亮指令演示 -->
        <h4>高亮指令 (背景颜色)</h4>
        <div class="directive-demo">
          <p>选择背景颜色：</p>
          <div class="color-buttons">
            <button @click="highlightColor = '#ffff99'" :class="{ active: highlightColor === '#ffff99' }">黄色</button>
            <button @click="highlightColor = '#90ee90'" :class="{ active: highlightColor === '#90ee90' }">浅绿色</button>
            <button @click="highlightColor = '#add8e6'" :class="{ active: highlightColor === '#add8e6' }">浅蓝色</button>
            <button @click="highlightColor = '#ffc0cb'" :class="{ active: highlightColor === '#ffc0cb' }">粉色</button>
          </div>
          <p v-highlight="highlightColor" class="highlight-text">
            这段文字使用了v-highlight指令，颜色会随着上方按钮点击而变化！
          </p>
          <p class="directive-explanation">
            原理：通过局部自定义指令v-highlight实现，在mounted和updated钩子中修改元素的背景色。
            当点击按钮改变highlightColor的值时，指令会自动更新元素的背景色。
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, shallowRef, nextTick } from 'vue'
import ComponentAExample from './experiment3/ComponentAExample.vue'
import ComponentBExample from './experiment3/ComponentBExample.vue'
import ComponentCExample from './experiment3/ComponentCExample.vue'
import BaseLayoutExample from './experiment3/BaseLayoutExample.vue'
import CardExample from './experiment3/CardExample.vue'
import ItemListExample from './experiment3/ItemListExample.vue'

// 动态组件
const currentComponent = shallowRef(ComponentAExample)
const ComponentA = shallowRef(ComponentAExample)
const ComponentB = shallowRef(ComponentBExample)
const ComponentC = shallowRef(ComponentCExample)

// 自定义指令相关变量
const highlightColor = ref('#ffff99') // 默认黄色

// 自定义指令：v-highlight
const vHighlight = {
  mounted(el, binding) {
    el.style.backgroundColor = binding.value
  },
  updated(el, binding) {
    el.style.backgroundColor = binding.value
  }
}

</script>

<style scoped>
/* 沿用实验二的样式 */
.example-section {
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
  margin: 0;
  color: #666;
  font-size: 0.9rem;
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

h4 {
  margin-top: 2rem;
  margin-bottom: 0.5rem;
  color: #333;
}

.scoped-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.scoped-item button {
  padding: 3px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* Added input style */
input[placeholder] {
  padding: 8px;
  width: 100%;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin: 10px 0;
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

.focus-input:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
  outline: none;
}

/* 动态组件容器样式 */
.dynamic-component-container {
  margin: 1rem 0;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #f9f9f9;
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
</style> 