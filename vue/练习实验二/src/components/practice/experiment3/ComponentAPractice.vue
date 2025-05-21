<template>
  <div class="dynamic-component">
    <h3>Component A</h3>
    <p>这是一个组件 A，请在此输入：</p>
    <!-- 学生需要绑定 v-model -->
    <input placeholder="请输入内容" />
  </div>
</template>

<script>
export default {
  name: 'ComponentAPractice'
}
</script>

<script setup>
// 学生需要在此处导入 ref, onActivated, onDeactivated
// import { ref, onActivated, onDeactivated } from 'vue'

// 学生需要定义 message ref
// const message = ref('')

// 学生需要实现 onActivated 和 onDeactivated 钩子
// onActivated(() => {
//   console.log('Component A Activated')
// })
// onDeactivated(() => {
//   console.log('Component A Deactivated')
// })
</script>

<style scoped>
.dynamic-component {
  border: 1px dashed #ccc;
  padding: 1rem;
  margin-top: 1rem;
}
input {
  margin-top: 10px;
  padding: 5px;
  width: 100%;
}
</style> 