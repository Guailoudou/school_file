<template>
  <div class="cross-level-demo">
    <h4>祖先组件</h4>
    <div class="component-box">
      <div class="message-box">
        <p>发送给后代组件的消息：</p>
        <input placeholder="输入要发送的消息" v-model="ancestorMessage" />
        <button @click="sendToDescendant">发送到后代组件</button>
      </div>
      <div class="message-display">
        <p>来自后代组件的消息：</p>
        <span>{{ descendantMessage }}</span>
      </div>
    </div>

    <!-- 学生需要在此处引入并使用 MiddleComponentPractice -->
    <MiddleComponentPractice />
  </div>
</template>

<script setup>
import { ref, provide } from 'vue'
import MiddleComponentPractice from './MiddleComponentPractice.vue'

const ancestorMessage = ref('')
const descendantMessage = ref('')

provide('ancestorMessage', ancestorMessage)
provide('handleDescendantResponse', (message) => {
  console.log('收到后代回复事件:', message)
  descendantMessage.value = message
})

function sendToDescendant() {
  console.log('发送到后代按钮点击')
}
</script>

<style scoped>
.cross-level-demo {
  border: 2px solid #42b983;
  border-radius: 8px;
  padding: 1rem;
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
  margin-top: 1rem;
  padding: 0.5rem;
  background: #f8f8f8;
  border-radius: 4px;
}
</style> 