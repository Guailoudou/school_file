<template>
  <div class="base-layout">
    <h4>基础布局组件</h4>
    <div class="content">
      <slot></slot> <!-- 默认插槽 -->
    </div>
  </div>
</template>

<style scoped>
.base-layout {
  border: 1px solid blue;
  padding: 1rem;
  margin-top: 1rem;
}
.content {
  background-color: #eef;
  padding: 1rem;
}
</style> 