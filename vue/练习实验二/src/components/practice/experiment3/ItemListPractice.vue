<template>
  <div class="item-list">
    <h4>列表组件</h4>
    <ul>
      <!-- 学生需要遍历 items 列表并使用作用域插槽 -->
      <li>
        <slot :item="{ id: 0, text: '示例项' }" :index="0">
          <!-- 默认内容，如果没有提供自定义模板 -->
          示例项
        </slot>
      </li>
    </ul>
  </div>
</template>

<script setup>
// 学生需要在此处导入 ref
// import { ref } from 'vue'

// 学生需要定义 items 列表
// const items = ref([
//   { id: 1, text: '学习 Vue 基础' },
//   { id: 2, text: '了解组件通信' },
//   { id: 3, text: '掌握插槽用法' }
// ])
</script>

<style scoped>
.item-list {
  border: 1px solid #42b983;
  padding: 1rem;
  margin-top: 1rem;
  border-radius: 8px;
}

ul {
  padding-left: 20px;
}

li {
  margin-bottom: 8px;
}
</style> 