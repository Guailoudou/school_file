<template>
  <div class="experiment">
    <div class="experiment-header">
      <h2>实验1：Vue.js基础</h2>
      <p class="experiment-description">
        学习Vue.js中的核心概念，包括单文件组件、数据绑定、内容渲染、属性绑定、双向绑定、
        条件渲染、列表渲染、事件处理、计算属性和侦听器
      </p>
    </div>
    
    <div class="experiment-container">
      <div class="example-container">
        <Experiment1Example />
      </div>
      <div class="practice-container">
        <Experiment1Practice />
      </div>
    </div>
  </div>
</template>

<script setup>
import Experiment1Example from '../components/examples/Experiment1Example.vue'
import Experiment1Practice from '../components/practice/Experiment1Practice.vue'
</script>

<style scoped>
.experiment {
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  font-size: 16px;
  box-sizing: border-box;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.experiment-header {
  text-align: center;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: linear-gradient(135deg, #42b983 0%, #33a06f 100%);
  border-radius: 12px;
  color: white;
  box-shadow: 0 4px 12px rgba(66, 185, 131, 0.2);
  transform: translateY(0);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experiment-header:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(66, 185, 131, 0.3);
}

.experiment h2 {
  color: white;
  margin-bottom: 1rem;
  font-size: 2.2rem;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.experiment-description {
  font-size: 1.1rem;
  opacity: 0.9;
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

.experiment-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 1rem;
  height: calc(100vh - 180px); /* 减少头部区域的高度 */
}

.example-container, .practice-container {
  transition: transform 0.3s ease;
  height: 100%;
  overflow: hidden; /* 防止内容溢出 */
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

.example-container:hover, .practice-container:hover {
  transform: translateY(-5px);
}

/* 响应式设计 */
@media (max-width: 1600px) {
  .experiment {
    padding: 1rem;
    font-size: 15px;
  }
  
  .experiment h2 {
    font-size: 2rem;
  }
  
  .experiment-container {
    height: calc(100vh - 170px);
  }
}

@media (max-width: 1440px) {
  .experiment {
    padding: 0.8rem;
    font-size: 14px;
  }
  
  .experiment h2 {
    font-size: 1.8rem;
  }
  
  .experiment-description {
    font-size: 1rem;
  }
  
  .experiment-container {
    height: calc(100vh - 160px);
  }
}

@media (max-width: 1200px) {
  .experiment {
    padding: 0.7rem;
  }
  
  .experiment-container {
    gap: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .experiment-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    height: auto; /* 在小屏幕上取消固定高度 */
  }
  
  .example-container, .practice-container {
    height: 500px; /* 调整固定高度 */
    margin-bottom: 1.5rem;
  }
  
  .experiment {
    padding: 0.8rem;
  }
  
  .experiment-header {
    margin-bottom: 1.5rem;
    padding: 0.8rem;
  }
}

@media (max-width: 768px) {
  .experiment {
    padding: 0.7rem;
    font-size: 13px;
  }

  .experiment h2 {
    font-size: 1.5rem;
    margin-bottom: 0.6rem;
  }
  
  .experiment-description {
    font-size: 0.9rem;
  }
  
  .experiment-header {
    padding: 0.8rem;
    margin-bottom: 1.2rem;
  }
  
  .experiment-container {
    gap: 1.5rem;
  }
  
  .example-container, .practice-container {
    height: 450px;
  }
}

@media (max-width: 480px) {
  .experiment {
    padding: 0.5rem;
    font-size: 12px;
  }
  
  .experiment h2 {
    font-size: 1.3rem;
  }
  
  .experiment-description {
    font-size: 0.85rem;
  }
  
  .experiment-header {
    padding: 0.7rem;
    margin-bottom: 1rem;
  }
  
  .experiment-container {
    gap: 1rem;
  }
  
  .example-container, .practice-container {
    height: 400px;
  }
}
</style> 