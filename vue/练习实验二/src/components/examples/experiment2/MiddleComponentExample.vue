<template>
  <div class="middle-component">
    <h4>中间组件</h4>
    <div class="component-box">
      <p class="note">我是中间组件，只负责传递消息</p>
    </div>
    <DescendantComponentExample />
  </div>
</template>

<script setup>
import DescendantComponentExample from './DescendantComponentExample.vue'
</script>

<style scoped>
.middle-component {
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

.note {
  color: #666;
  font-style: italic;
}
</style> 