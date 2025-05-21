<template>
  <div class="child-component">
    <h4>子组件</h4>
    <div class="component-box">
      <div class="message-display" v-if="message">
        <p>收到父组件消息：{{ message }}</p>
      </div>
      <div class="message-box">
        <p>回复父组件：</p>
        <input v-model="responseMessage" placeholder="输入要回复的消息" />
        <button @click="sendToParent">回复到父组件</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'

const props = defineProps({
  message: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['response'])
const responseMessage = ref('')

function sendToParent() {
  if (!responseMessage.value) {
    alert('请输入要回复的消息')
    return
  }
  emit('response', responseMessage.value)
  responseMessage.value = ''
}
</script>

<style scoped>
.child-component {
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