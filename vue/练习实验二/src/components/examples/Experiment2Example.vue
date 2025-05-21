<template>
  <div class="example-section">
    <h2 class="main-title">示例区域</h2>
    
    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>实验概述</h4>
      <div class="intro-content">
        <p>本实验展示了Vue 3中组件间通信的多种方式，帮助您理解不同组件之间如何进行数据传递和交互。</p>
        <p>通过这些示例，您将学习父子组件通信和跨级组件通信的实现方式，掌握Vue组件间协同工作的基本原理。</p>
        <p>每个示例都提供了可交互的演示，您可以直接体验不同通信机制的效果。</p>
      </div>
    </section>
    
    <div class="experiment-section">
      <h3>1. 父子组件通信</h3>
      <div class="experiment-desc">本实验演示了父组件与子组件之间的数据传递。父组件通过props向下传递数据给子组件，子组件通过emit事件向上通知父组件，实现双向通信机制。</div>
      <div class="content-box">
        <div class="description">
          <p>通过 props 和 emit 实现父子组件之间的通信</p>
        </div>
        <ParentChildDemoExample />
      </div>
    </div>
    
    <div class="experiment-section">
      <h3>2. 跨级组件通信</h3>
      <div class="experiment-desc">本实验展示了祖先组件与后代组件间的数据传递。无需通过中间组件层层传递数据，祖先组件使用provide提供数据，后代组件使用inject注入并使用这些数据。</div>
      <div class="content-box">
        <div class="description">
          <p>通过 provide/inject 实现跨级组件之间的通信</p>
        </div>
        <CrossLevelDemoExample />
      </div>
    </div>
  </div>
</template>

<script setup>
import ParentChildDemoExample from './experiment2/ParentChildDemoExample.vue'
import CrossLevelDemoExample from './experiment2/CrossLevelDemoExample.vue'
</script>

<style scoped>
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

.example-section::-webkit-scrollbar {
  width: 8px;
}

.example-section::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.example-section::-webkit-scrollbar-thumb {
  background: #42b983;
  border-radius: 4px;
}

.example-section::-webkit-scrollbar-thumb:hover {
  background: #2f9c69;
}

.example-section:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
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

code {
  font-family: 'Courier New', Courier, monospace;
  background-color: #f1f1f1;
  padding: 2px 4px;
  border-radius: 3px;
  color: #e83e8c;
}

.control-panel {
  display: flex;
  justify-content: center;
  padding: 2rem;
}

.demo-button {
  background: linear-gradient(135deg, #42b983, #2f9c69);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s;
}

.demo-button:hover {
  background: linear-gradient(135deg, #3ca876, #278a5b);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .main-title {
    font-size: 1.5rem;
  }
  
  .experiment-section h3 {
    font-size: 1.2rem;
  }
}
</style> 