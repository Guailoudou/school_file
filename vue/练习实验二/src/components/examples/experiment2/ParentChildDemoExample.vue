<template>
  <div class="parent-component">
    <h4>父组件</h4>
    <div class="component-box">
      <div class="message-box">
        <p>发送给子组件的消息：</p>
        <input v-model="parentMessage" placeholder="输入要发送的消息" />
        <button @click="sendToChild">发送到子组件</button>
      </div>
      <div class="message-display" v-if="childMessage">
        <p>来自子组件的消息：{{ childMessage }}</p>
      </div>
    </div>

    <ChildComponentExample 
      :message="parentMessage"
      @response="handleChildResponse"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildComponentExample from './ChildComponentExample.vue'

const parentMessage = ref('')
const childMessage = ref('')

function sendToChild() {
  if (!parentMessage.value) {
    alert('请输入要发送的消息')
    return
  }
}

function handleChildResponse(message) {
  childMessage.value = message
}
</script>

<style scoped>
.parent-component {
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