<template>
  <div class="dynamic-component">
    <h3>Component C</h3>
    <p>这是一个组件 C。</p>
    <p>计数器: {{ count }}</p>
    <button @click="count++">增加</button>
  </div>
</template>

<script>
export default {
  name: 'ComponentCExample'
}
</script>

<script setup>
import { ref, onActivated, onDeactivated } from 'vue'
const count = ref(0)
onActivated(() => {
  console.log('Component C Activated')
})
onDeactivated(() => {
  console.log('Component C Deactivated')
})
</script>

<style scoped>
.dynamic-component {
  border: 1px dashed #ccc;
  padding: 1rem;
  margin-top: 1rem;
}
button {
  margin-left: 5px;
}
</style> 