<template>
  <div class="dynamic-component">
    <h3>Component A</h3>
    <p>这是一个组件 A。</p>
    <input type="text" placeholder="在 A 中输入内容" />
  </div>
</template>

<script>
export default {
  name: 'ComponentAExample'
}
</script>

<script setup>
import { onActivated, onDeactivated } from 'vue'
onActivated(() => {
  console.log('Component A Activated')
})
onDeactivated(() => {
  console.log('Component A Deactivated')
})
</script>

<style scoped>
.dynamic-component {
  border: 1px dashed #ccc;
  padding: 1rem;
  margin-top: 1rem;
}
input {
  margin-top: 0.5rem;
  padding: 5px;
}
</style> 