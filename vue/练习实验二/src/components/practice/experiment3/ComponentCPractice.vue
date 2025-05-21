<template>
  <div class="dynamic-component">
    <h3>Component C</h3>
    <p>这是一个组件 C。</p>
    <!-- 学生需要显示 count 值 -->
    <p>计数器: </p>
    <!-- 学生需要绑定 click 事件 -->
    <button>增加</button>
  </div>
</template>

<script>
export default {
  name: 'ComponentCPractice'
}
</script>

<script setup>
// 学生需要在此处导入 ref, onActivated, onDeactivated
// import { ref, onActivated, onDeactivated } from 'vue'

// 学生需要定义 count ref
// const count = ref(0)

// 学生需要实现增加 count 的方法
// const increment = () => { count.value++ }

// 学生需要实现 onActivated 和 onDeactivated 钩子
// onActivated(() => {
//   console.log('Component C Activated')
// })
// onDeactivated(() => {
//   console.log('Component C Deactivated')
// })
</script>

<style scoped>
.dynamic-component {
  border: 1px dashed #ccc;
  padding: 1rem;
  margin-top: 1rem;
}
button {
  margin-left: 5px;
  padding: 5px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #3aa876;
}
</style> 