<template>
  <div class="descendant-component">
    <h4>后代组件</h4>
    <div class="component-box">
      <div class="message-display">
        <p>收到祖先组件消息：</p>
      </div>
      <div class="message-box">
        <p>回复祖先组件：</p>
        <input placeholder="输入要回复的消息" />
        <button>回复到祖先组件</button>
      </div>
    </div>
  </div>
</template>

<script setup>
// import { ref, inject } from 'vue'

// 学生需要在此处注入 ancestorMessage 和 handleDescendantResponse
// const ancestorMessage = inject('ancestorMessage')
// const handleDescendantResponse = inject('handleDescendantResponse')

// 学生需要在此处定义响应式变量来存储回复消息
// const responseMessage = ref('')

// 学生需要在此处定义方法来处理发送回复
// function sendToAncestor() { ... }
</script>

<style scoped>
.descendant-component {
  border: 2px solid #42b983;
  border-radius: 8px;
  padding: 1rem;
  margin-top: 1rem;
}

.component-box {
  background-color: white;
  padding: 1rem;
  border-radius: 6px;
  margin: 1rem 0;
}

h4 {
  color: #2c3e50;
  margin: 0 0 1rem 0;
}

.message-box {
  margin-bottom: 1rem;
}

input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 8px;
  width: 200px;
}

button {
  background: #42b983;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background: #3aa876;
}

.message-display {
  margin-bottom: 1rem;
  padding: 0.5rem;
  background: #f8f8f8;
  border-radius: 4px;
}
</style> 