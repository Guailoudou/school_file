<script setup>
import HelloWorld from './components/HelloWorld.vue'
import xxjhb from './components/sy1/xxjhb.vue'
import todolist from './components/sy2/todolist.vue'
import CAPI from './components/CAPI.vue'

</script>

<template>
  <!-- <HelloWorld/> -->
  <!-- <xxjhb/> -->
    <todolist/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
