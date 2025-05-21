<template>
  <div class="item-list">
    <h4>列表组件</h4>
    <ul>
      <li v-for="(item, index) in items" :key="item.id">
        <slot :item="item" :index="index">
          <!-- 默认内容，如果没有提供自定义模板 -->
          {{ item.text }}
        </slot>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, text: '学习 Vue 基础' },
  { id: 2, text: '了解组件通信' },
  { id: 3, text: '掌握插槽用法' },
  { id: 4, text: '实践自定义指令' }
])
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