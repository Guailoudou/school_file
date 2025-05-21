<template>
  <div class="practice-section">
    <h2 class="main-title">练习区域</h2>
    
    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>练习概述</h4>
      <div class="intro-content">
        <p>本练习区域提供了与示例区域对应的实践任务，帮助您巩固所学的Vue 3组件通信知识。</p>
        <p>请尝试实现父子组件通信和跨级组件通信的功能，将理论知识转化为实际编码能力。</p>
        <p>通过这些练习，您将深入理解Vue组件间的数据流动和交互方式。</p>
      </div>
    </section>
    
    <div class="experiment-section">
      <h3>1. 父子组件通信练习</h3>
      <div class="experiment-desc">本练习要求您实现父组件与子组件之间的双向通信。在实践中，您将学习如何通过props向下传递数据，并通过事件emit向上传递信息，构建清晰的组件通信模型。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现父子组件之间的通信：</p>
          <ul>
            <li>使用 props 从父组件向子组件传递数据</li>
            <li>使用 emit 从子组件向父组件发送事件</li>
          </ul>
        </div>
        <ParentChildDemoPractice />
      </div>
    </div>
    
    <div class="experiment-section">
      <h3>2. 跨级组件通信练习</h3>
      <div class="experiment-desc">本练习要求您实现祖先组件与后代组件之间的数据传递。您将学习如何使用provide/inject机制，避免通过中间组件传递数据，解决深层组件通信的问题。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现跨级组件之间的通信：</p>
          <ul>
            <li>使用 provide 在祖先组件中提供数据</li>
            <li>使用 inject 在后代组件中注入数据</li>
          </ul>
        </div>
        <CrossLevelDemoPractice />
      </div>
    </div>
  </div>
</template>

<script setup>
import ParentChildDemoPractice from './experiment2/ParentChildDemoPractice.vue'
import CrossLevelDemoPractice from './experiment2/CrossLevelDemoPractice.vue'
</script>

<style scoped>
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

code {
  font-family: 'Courier New', Courier, monospace;
  background-color: #f1f1f1;
  padding: 2px 4px;
  border-radius: 3px;
  color: #e83e8c;
}

@media (max-width: 768px) {
  .practice-section {
    padding: 1.2rem;
  }
  
  .main-title {
    font-size: 1.5rem;
  }
  
  .experiment-section h3 {
    font-size: 1.2rem;
  }
  
  .content-box {
    padding: 1.2rem;
  }
}

@media (max-width: 480px) {
  .practice-section {
    padding: 1rem;
  }
  
  .content-box {
    padding: 1rem;
  }
}
</style> 