<script setup>
import { ref } from 'vue'

// defineProps({
//   msg: String,
// })

// const count = ref(0)
const msg = 'Hello World'
const hmsg = '<h2>Hello World</h2>'

const username = '请输入用户名'
const password = '请输入密码'

const showInfo = () => {
  console.log('欢迎来到Vue.js的世界！')
}
const username2 = ref('zhangsan')

const n1 = ref(1)
const n2 = ref(2)
const n11 = ref(1)
const n22 = ref(2)

const type = ref('B')

const flag = ref(true)

</script>

<template>
  <h2>{{ msg }}</h2>
  <div v-text="msg"></div>
  <div v-html="hmsg"></div>
  <p><input type="text" v-bind:placeholder="username"></p>
  <p><input type="password" :placeholder="password"></p>
  <button @click="showInfo">输出信息</button>
  <hr>
  请输入姓名：<input type="text" v-model="username2">
  <div>姓名是：{{ username2 }}</div>
  <hr>
  <input type="text" v-model="n1"> + <input type="text" v-model="n2"> = {{ n1 + n2 }}
  <input type="text" v-model.number="n11"> + <input type="text" v-model.number="n22"> = {{ n11 + n22 }}
  <hr>
  小明的学习评定等级为：
  <p v-if="type === 'A'">优秀</p>
  <p v-else-if="type === 'B'">良好</p>
  <p v-else>差</p>
  <button @click="type = 'A'">切换成优秀</button>
  <button @click="type = 'B'">切换成良好</button>
  <button @click="type = 'C'">切换成差</button>
  <hr>
  <p v-if="flag">通过v-if控制的元素</p>
  <p v-show="flag">通过v-show控制的元素</p>
  <button @click="flag = !flag">显示/隐藏</button>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
