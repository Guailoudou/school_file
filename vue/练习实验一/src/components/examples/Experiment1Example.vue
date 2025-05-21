<template>
  <div class="example-section">
    <h3>完整示例</h3>
    
    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>实验概述</h4>
      <div class="intro-content">
        <p>本实验展示了Vue 3的核心特性和基本用法，帮助您快速了解Vue框架的主要功能。</p>
        <p>通过以下10个小实验，您将学习单文件组件结构、数据绑定、指令系统、事件处理等Vue的基础知识。</p>
        <p>每个实验都包含可交互的示例，您可以直接操作查看效果。</p>
      </div>
    </section>
    
    <!-- 1. 单文件组件 -->
    <section class="experiment-section">
      <h4>1. 单文件组件</h4>
      <div class="experiment-desc">本实验展示了Vue文件的三大组成部分。查看当前文件结构，了解模板、脚本和样式如何协同工作构成一个完整组件。</div>
      <div class="demo-box">
        <!-- 说明Vue单文件组件的基本结构 -->
        <p>当前文件是一个Vue单文件组件(.vue)，包含模板(template)、脚本(script)和样式(style)三部分</p>
        <div class="file-structure">
          <!-- 模板部分说明 -->
          <div class="file-part">
            <span class="file-label">template</span>
            <span>HTML结构</span>
          </div>
          <!-- 脚本部分说明 -->
          <div class="file-part">
            <span class="file-label">script</span>
            <span>JavaScript逻辑</span>
          </div>
          <!-- 样式部分说明 -->
          <div class="file-part">
            <span class="file-label">style</span>
            <span>CSS样式</span>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 2. 数据绑定 -->
    <section class="experiment-section">
      <h4>2. 数据绑定</h4>
      <div class="experiment-desc">本实验演示数据与界面的绑定关系。在输入框中输入任意文本，观察下方文本内容和长度如何实时更新，体验Vue的响应式系统。</div>
      <div class="demo-box">
        <!-- 步骤1: 在此输入框中输入任意文本 -->
        <!-- v-model指令实现了表单输入和变量的双向绑定 -->
        <input type="text" v-model="exampleMessage" placeholder="输入消息">
        
        <!-- 步骤2: 观察下方文本如何随着输入实时更新 -->
        <!-- 这里使用双大括号语法进行文本插值，将变量值渲染到DOM中 -->
        <p>消息：{{ exampleMessage }}</p>
        
        <!-- 步骤3: 观察文本长度如何随着输入自动计算并更新 -->
        <!-- 这里使用计算属性自动计算文本长度，计算属性会随依赖变化而更新 -->
        <p>消息长度：{{ exampleMessageLength }}</p>

        <!-- 实验说明：当输入框内容改变时，Vue自动更新相关联的DOM部分，无需手动操作DOM -->
      </div>
    </section>

    <!-- 3. 内容渲染指令 v-text 和 v-html -->
    <section class="experiment-section">
      <h4>3. 内容渲染指令</h4>
      <div class="experiment-desc">本实验展示两种内容渲染方式的区别。在输入框中输入HTML标签（如&lt;b&gt;粗体&lt;/b&gt;），观察v-text将其作为纯文本显示，而v-html会解析并渲染HTML标签。</div>
      <div class="demo-box">
        <h5>v-text指令</h5>
        <!-- 步骤1: 查看此处如何使用v-text渲染文本 -->
        <!-- v-text指令将变量内容作为纯文本渲染，不解析HTML标签 -->
        <!-- 这里显示的是与第二个实验相同的变量内容 -->
        <p v-text="exampleMessage"></p>
        
        <h5>v-html指令</h5>
        <!-- 步骤2: 在此输入框中输入一些HTML标签，如<b>粗体文本</b>或<span style="color:red">红色文本</span> -->
        <!-- v-model实现输入框与变量的双向绑定 -->
        <input type="text" v-model="exampleHtmlContent" placeholder="输入HTML内容 (如: <b>粗体</b>)">
        
        <!-- 步骤3: 观察下方内容如何渲染HTML标签 -->
        <!-- v-html指令会解析HTML内容并渲染，可能存在XSS风险，谨慎使用 -->
        <div v-html="exampleHtmlContent" class="html-preview"></div>

        <!-- 实验说明：v-text适用于纯文本渲染，v-html适用于需要渲染HTML的场景 -->
      </div>
    </section>

    <!-- 4. 属性绑定指令 v-bind -->
    <section class="experiment-section">
      <h4>4. 属性绑定指令</h4>
      <div class="experiment-desc">本实验演示如何动态绑定HTML元素的属性值。在链接地址输入框中输入URL，观察链接的href属性如何更新；在颜色选择器中选择一个颜色，右侧色块会实时更新为所选颜色；点击按钮可切换激活状态，体验类名的动态绑定。</div>
      <div class="demo-box">
        <h5>v-bind指令</h5>
        <!-- 用户输入与变量的双向绑定 -->
        <input type="text" v-model="exampleLink" placeholder="输入链接地址">
        <div class="link-wrapper">
          <!-- v-bind将变量值绑定到HTML属性 -->
          <a v-bind:href="exampleLink" target="_blank">链接</a> 
          <span class="shorthand-note">(:href 是 v-bind:href 的简写)</span>
        </div>
        
        <h5>样式绑定</h5>
        <div class="color-picker">
          <!-- 颜色选择器与变量双向绑定 -->
          <input type="color" v-model="exampleColor">
          <!-- 使用v-bind:style绑定内联样式 -->
          <div class="color-box" :style="{ backgroundColor: exampleColor }"></div>
        </div>
        <p>当前颜色：{{ exampleColor }}</p>
        
        <h5>class绑定</h5>
        <!-- 根据isActive变量状态动态添加或移除active类 -->
        <button @click="toggleActive" :class="{ active: isActive }">
          {{ isActive ? '激活状态' : '未激活状态' }}
        </button>
      </div>
    </section>

    <!-- 5. 双向绑定指令 v-model -->
    <section class="experiment-section">
      <h4>5. 双向绑定指令</h4>
      <div class="experiment-desc">本实验展示v-model在不同表单元素上的应用。在文本框中输入内容，下方立即显示；勾选复选框，状态文本随之变化；从下拉列表选择一个选项，选择结果立即更新。</div>
      <div class="demo-box">
        <h5>v-model 基本用法</h5>
        <!-- 文本输入框的双向数据绑定 -->
        <input type="text" v-model="exampleInputText" placeholder="输入文本">
        <p>输入的内容：{{ exampleInputText }}</p>
        
        <h5>v-model 用于复选框</h5>
        <div class="checkbox-group">
          <label>
            <!-- 复选框状态与布尔变量的双向绑定 -->
            <input type="checkbox" v-model="exampleChecked"> 是否选中
          </label>
          <p>复选框状态：{{ exampleChecked ? '已选中' : '未选中' }}</p>
        </div>
        
        <h5>v-model 用于选择框</h5>
        <!-- 选择框与变量的双向绑定 -->
        <select v-model="exampleSelected">
          <option value="">请选择</option>
          <option value="A">选项A</option>
          <option value="B">选项B</option>
          <option value="C">选项C</option>
        </select>
        <p>当前选择：{{ exampleSelected || '无' }}</p>
      </div>
    </section>

    <!-- 6. 条件渲染指令 v-if 和 v-show -->
    <section class="experiment-section">
      <h4>6. 条件渲染指令</h4>
      <div class="experiment-desc">本实验演示条件渲染的两种方式。在分数输入框中输入不同分数，观察下方文本如何根据分数范围显示不同评级；在用户名框中输入名称并点击登录，界面会切换到已登录状态，点击退出可返回登录界面。</div>
      <div class="demo-box">
        <h5>v-if / v-else-if / v-else 指令</h5>
        <div class="score-input">
          <!-- 数字输入与变量的双向绑定 -->
          <input type="number" v-model="exampleScore" placeholder="输入分数(0-100)">
        </div>
        <div class="result-display">
          <!-- 条件渲染：根据分数值显示不同内容 -->
          <p v-if="exampleScore >= 90">优秀！</p>
          <p v-else-if="exampleScore >= 80">良好！</p>
          <p v-else-if="exampleScore >= 60">及格！</p>
          <p v-else-if="exampleScore >= 0">不及格！</p>
          <p v-else>请输入有效分数</p>
        </div>
        
        <h5>v-show 指令</h5>
        <div class="login-simulation">
          <!-- v-show通过CSS的display属性控制元素显隐 -->
          <div v-show="!exampleLoggedIn">
            <input type="text" v-model="exampleUsername" placeholder="用户名">
            <button @click="exampleLogin">登录</button>
          </div>
          <div v-show="exampleLoggedIn">
            <p>欢迎回来，{{ exampleUsername }}！</p>
            <button @click="exampleLogout">退出登录</button>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 列表渲染指令 v-for -->
    <section class="experiment-section">
      <h4>7. 列表渲染指令</h4>
      <div class="experiment-desc">本实验展示列表数据的渲染。在输入框中输入内容并点击添加，新项目会添加到列表中；点击任意项目的删除按钮可将其移除；下方示例展示了如何遍历对象的属性和值。</div>
      <div class="demo-box">
        <h5>v-for 基本用法</h5>
        <div class="list-controls">
          <!-- 新项目输入与变量绑定 -->
          <input type="text" v-model="exampleNewItem" placeholder="添加项目">
          <button @click="exampleAddItem">添加</button>
        </div>
        <ul class="demo-list">
          <!-- v-for循环渲染数组，:key提供唯一标识 -->
          <li v-for="(item, index) in exampleItems" :key="item.id">
            {{ index + 1 }}. {{ item.text }}
            <button class="delete-btn" @click="exampleRemoveItem(item.id)">删除</button>
          </li>
        </ul>
        <!-- 条件渲染：列表为空时显示提示 -->
        <p v-if="exampleItems.length === 0" class="empty-list">列表为空</p>
        
        <h5>v-for 与对象</h5>
        <ul class="demo-list">
          <!-- 遍历对象的属性和值 -->
          <li v-for="(value, key) in examplePerson" :key="key">
            {{ key }}: {{ value }}
          </li>
        </ul>
      </div>
    </section>

    <!-- 8. 事件处理指令 v-on -->
    <section class="experiment-section">
      <h4>8. 事件处理指令</h4>
      <div class="experiment-desc">本实验演示事件处理机制。点击加减按钮可增减计数器的值；在事件冒泡示例中，点击内层容器时仅触发内层事件，点击外层容器会触发外层事件；在输入框中输入文本并按Enter键，输入内容会显示在下方。</div>
      <div class="demo-box">
        <h5>v-on 基本用法</h5>
        <div class="counter">
          <!-- v-on:click绑定点击事件处理函数 -->
          <button v-on:click="exampleDecrement">-</button>
          <span>{{ exampleCounter }}</span>
          <!-- @click是v-on:click的简写形式 -->
          <button @click="exampleIncrement">+</button>
          <span class="shorthand-note">(@click 是 v-on:click 的简写)</span>
        </div>
        
        <h5>事件修饰符</h5>
        <div class="event-modifiers">
          <!-- 普通点击事件 -->
          <div class="bubble-container" @click="exampleHandleBubble">
            <p>外层容器 (点击我)</p>
            <!-- .stop修饰符阻止事件冒泡 -->
            <div class="bubble-inner" @click.stop="exampleHandleInner">
              <p>内层容器 (点击我，事件不会冒泡)</p>
            </div>
          </div>
          <p>事件触发：{{ exampleBubbleResult }}</p>
        </div>
        
        <h5>按键修饰符</h5>
        <div class="key-modifiers">
          <!-- .enter修饰符指定按下Enter键时触发事件 -->
          <input 
            type="text" 
            v-model="exampleKeyInput"
            @keyup.enter="exampleSubmitInput"
            placeholder="输入文本并按Enter提交"
          >
          <p>提交结果：{{ exampleKeyResult }}</p>
        </div>
      </div>
    </section>

    <!-- 9. 计算属性 -->
    <section class="experiment-section">
      <h4>9. 计算属性</h4>
      <div class="experiment-desc">本实验展示计算属性的特性。在输入框中输入数字，自动计算并显示其平方、立方和奇偶性；点击"触发重新渲染"按钮多次，观察计算属性和方法调用次数的差异，体验计算属性的缓存机制。</div>
      <div class="demo-box">
        <!-- 数字输入与变量绑定 -->
        <input type="number" v-model="exampleNumber" placeholder="输入数字">
        <!-- 计算属性自动根据输入值计算结果 -->
        <p>平方：{{ exampleSquare }}</p>
        <p>立方：{{ exampleCube }}</p>
        <p>是否偶数：{{ exampleIsEven ? '是' : '否' }}</p>
        
        <h5>计算属性 vs 方法</h5>
        <p>计算属性会缓存，当依赖项不变时不会重新计算</p>
        <p>计算次数(计算属性)：{{ exampleComputedCount }}</p>
        <p>计算次数(方法)：{{ exampleMethodCount() }}</p>
        <button @click="triggerRender">触发重新渲染</button>
      </div>
    </section>

    <!-- 10. 侦听器 -->
    <section class="experiment-section">
      <h4>10. 侦听器</h4>
      <div class="experiment-desc">本实验演示数据变化的监听机制。在输入框中输入内容并修改，观察变化次数的增加以及历史记录的更新，体验Vue如何捕获数据变化并执行相应操作。</div>
      <div class="demo-box">
        <h5>侦听数据变化</h5>
        <!-- 输入框与被侦听的变量绑定 -->
        <input type="text" v-model="exampleWatchedValue" placeholder="修改此值会触发侦听器">
        <!-- 展示变化次数和历史记录 -->
        <p>值变化次数：{{ exampleWatchCount }}</p>
        <p>历史变化：</p>
        <ul class="history-list">
          <!-- 遍历并显示变化历史 -->
          <li v-for="(item, index) in exampleWatchHistory" :key="index">
            {{ item }}
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// 实验2: 数据绑定
const exampleMessage = ref('Hello Vue!') // 创建响应式变量，用于数据绑定示例
// 计算属性：根据exampleMessage的值自动计算字符长度
// 当exampleMessage变化时，此计算属性会自动重新计算
const exampleMessageLength = computed(() => exampleMessage.value.length) 

// 实验3: 内容渲染
// 初始值包含HTML标签，用于演示v-html的效果
// 这是一个响应式变量，它的变化会触发相关DOM的更新
const exampleHtmlContent = ref('<span style="color: red">这是HTML内容</span>') 

// 实验4: 属性绑定
const exampleLink = ref('https://vuejs.org') // 链接地址的响应式变量
const exampleColor = ref('#42b983') // 颜色值的响应式变量
const isActive = ref(false) // 按钮状态的响应式变量
const toggleActive = () => {
  isActive.value = !isActive.value // 切换按钮激活状态
}

// 实验5: 双向绑定
const exampleInputText = ref('') // 文本输入的响应式变量
const exampleChecked = ref(false) // 复选框状态的响应式变量
const exampleSelected = ref('') // 选择框值的响应式变量

// 实验6: 条件渲染
const exampleScore = ref(75) // 成绩分数的响应式变量
const exampleLoggedIn = ref(false) // 登录状态的响应式变量
const exampleUsername = ref('') // 用户名的响应式变量
const exampleLogin = () => {
  if (exampleUsername.value.trim()) {
    exampleLoggedIn.value = true // 更新登录状态
  }
}
const exampleLogout = () => {
  exampleLoggedIn.value = false // 退出登录
}

// 实验7: 列表渲染
const exampleItems = ref([
  { id: 1, text: '学习Vue基础' },
  { id: 2, text: '掌握组件通信' },
  { id: 3, text: '了解Vue Router' }
]) // 列表项的响应式数组
const exampleNewItem = ref('') // 新列表项的输入值
let nextId = 4 // 下一个项目的ID

const exampleAddItem = () => {
  if (exampleNewItem.value.trim()) {
    exampleItems.value.push({
      id: nextId++,
      text: exampleNewItem.value
    }) // 添加新项目到数组
    exampleNewItem.value = '' // 清空输入框
  }
}

const exampleRemoveItem = (id) => {
  exampleItems.value = exampleItems.value.filter(item => item.id !== id) // 通过过滤删除指定项目
}

const examplePerson = ref({
  name: '张三',
  age: 28,
  job: '前端开发'
}) // 对象类型的响应式变量，用于v-for示例

// 实验8: 事件处理
const exampleCounter = ref(0) // 计数器的响应式变量
const exampleIncrement = () => {
  exampleCounter.value++ // 计数器加1
}
const exampleDecrement = () => {
  exampleCounter.value-- // 计数器减1
}

const exampleBubbleResult = ref('') // 事件冒泡结果的响应式变量
const exampleHandleBubble = () => {
  exampleBubbleResult.value = '外层容器被点击' // 外层事件处理
}
const exampleHandleInner = () => {
  exampleBubbleResult.value = '内层容器被点击 (阻止冒泡)' // 内层事件处理(阻止冒泡)
}

const exampleKeyInput = ref('') // 按键输入的响应式变量
const exampleKeyResult = ref('') // 按键结果的响应式变量
const exampleSubmitInput = () => {
  exampleKeyResult.value = exampleKeyInput.value // 提交输入内容
  exampleKeyInput.value = '' // 清空输入框
}

// 实验9: 计算属性
const exampleNumber = ref(0) // 数字输入的响应式变量
const exampleSquare = computed(() => exampleNumber.value * exampleNumber.value) // 计算平方
const exampleCube = computed(() => exampleNumber.value * exampleNumber.value * exampleNumber.value) // 计算立方
const exampleIsEven = computed(() => exampleNumber.value % 2 === 0) // 判断是否为偶数

const renderTrigger = ref(0) // 触发重新渲染的响应式变量
const triggerRender = () => {
  renderTrigger.value++ // 增加值以触发页面重新渲染
}

let methodCountValue = 0 // 方法调用计数
const exampleComputedCount = computed(() => {
  console.log('计算属性被重新计算')
  return exampleNumber.value + renderTrigger.value * 0 // 依赖于exampleNumber和renderTrigger
})

const exampleMethodCount = () => {
  console.log('方法被调用')
  methodCountValue++
  return methodCountValue // 每次调用都会增加计数
}

// 实验10: 侦听器
const exampleWatchedValue = ref('') // 被侦听的响应式变量
const exampleWatchCount = ref(0) // 变化次数的响应式变量
const exampleWatchHistory = ref([]) // 变化历史的响应式数组

// 监听exampleWatchedValue的变化
watch(exampleWatchedValue, (newValue, oldValue) => {
  exampleWatchCount.value++ // 增加变化计数
  exampleWatchHistory.value.push(`${oldValue} → ${newValue}`) // 记录变化历史
  // 只保留最近5条记录
  if (exampleWatchHistory.value.length > 5) {
    exampleWatchHistory.value.shift() // 移除最早的记录
  }
})
</script>

<style scoped>
.example-section {
  background-color: white;
  padding: 1rem 1.2rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  height: 100%;
  transition: box-shadow 0.3s ease;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: #42b983 #f1f1f1;
}

/* 实验介绍样式 */
.experiment-introduction {
  margin: 0.5rem 0 1.5rem 0;
  padding: 1rem 1.2rem;
  background-color: #f0f7f4;
  border-left: 4px solid #42b983;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experiment-introduction:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(66, 185, 131, 0.1);
}

.experiment-introduction h4 {
  color: #2c3e50;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.intro-content p {
  margin: 0.6rem 0;
  line-height: 1.6;
  color: #34495e;
}

.example-section:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.example-section h3 {
  color: #2c3e50;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
  font-size: 1.5rem;
  position: relative;
  padding-bottom: 0.6rem;
}

.example-section h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #42b983, #33a06f);
  border-radius: 2px;
}

.experiment-section {
  margin: 1rem 0;
  padding: 0.8rem 1rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experiment-section:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.experiment-section h4 {
  color: #2c3e50;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
}

.experiment-section h4::before {
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: #42b983;
  border-radius: 50%;
  margin-right: 0.8rem;
}

.experiment-section h5 {
  color: #2c3e50;
  margin: 1rem 0 0.6rem;
  font-size: 1rem;
  border-left: 3px solid #42b983;
  padding-left: 0.8rem;
}

.demo-box {
  padding: 0.8rem 1rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}

/* 单文件组件样式 */
.file-structure {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  margin-top: 1rem;
}

.file-part {
  display: flex;
  align-items: center;
  padding: 0.8rem;
  background-color: #f8f9fa;
  border-radius: 6px;
}

.file-label {
  background-color: #42b983;
  color: white;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  margin-right: 0.8rem;
  font-family: monospace;
}

/* 内容渲染样式 */
.html-preview {
  margin-top: 0.8rem;
  padding: 0.8rem;
  background-color: #f8f9fa;
  border-radius: 6px;
  border: 1px dashed #ddd;
}

/* 属性绑定样式 */
.color-picker {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 1rem 0;
}

.color-box {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease;
}

.color-box:hover {
  transform: scale(1.05);
}

.link-wrapper {
  margin: 0.8rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* 类绑定样式 */
button.active {
  background: linear-gradient(135deg, #42b983 0%, #33a06f 100%);
  color: white;
}

/* 条件渲染样式 */
.score-input {
  margin-bottom: 0.8rem;
}

.result-display {
  padding: 0.8rem;
  background-color: #f8f9fa;
  border-radius: 6px;
  min-height: 1.5rem;
}

.login-simulation {
  margin-top: 1rem;
  padding: 0.8rem;
  background-color: #f8f9fa;
  border-radius: 6px;
}

/* 列表渲染样式 */
.list-controls {
  display: flex;
  gap: 0.8rem;
  margin-bottom: 1rem;
}

.demo-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.demo-list li {
  display: flex;
  justify-content: space-between;
  padding: 0.6rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  transition: background-color 0.2s ease;
}

.demo-list li:hover {
  background-color: #e9ecef;
}

.delete-btn {
  background-color: #f8d7da;
  color: #721c24;
  border: none;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
}

.delete-btn:hover {
  background-color: #f5c6cb;
}

.empty-list {
  text-align: center;
  color: #6c757d;
  font-style: italic;
}

/* 事件处理样式 */
.counter {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.counter button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background-color: #42b983;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.counter button:hover {
  background-color: #33a06f;
}

.shorthand-note {
  color: #6c757d;
  font-size: 0.8rem;
  font-style: italic;
  margin-left: 0.5rem;
}

.bubble-container {
  padding: 1.2rem;
  background-color: #e9ecef;
  border-radius: 6px;
  cursor: pointer;
  margin: 1rem 0;
}

.bubble-inner {
  padding: 1rem;
  background-color: #dee2e6;
  border-radius: 4px;
  margin-top: 0.8rem;
  cursor: pointer;
}

/* 通用表单样式 */
input[type="text"], input[type="number"] {
  width: 100%;
  padding: 0.8rem;
  margin: 0.8rem 0;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

input[type="color"] {
  width: 50px;
  height: 50px;
  padding: 0;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

select {
  width: 100%;
  padding: 0.8rem;
  margin: 0.8rem 0;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  background-color: white;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus, input[type="number"]:focus, select:focus {
  outline: none;
  border-color: #42b983;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
}

button {
  background-color: #e9ecef;
  color: #2c3e50;
  border: none;
  padding: 0.8rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

button:hover {
  background-color: #dee2e6;
}

.checkbox-group {
  margin: 1rem 0;
}

.demo-box p {
  margin: 0.8rem 0;
  color: #2c3e50;
  padding: 0.5rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.demo-box p:hover {
  background-color: #e9ecef;
}

/* 侦听器样式 */
.history-list {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.history-list li {
  margin-bottom: 0.3rem;
}

/* 响应式设计 */
@media (max-width: 1600px) {
  .example-section {
    font-size: 15px;
  }
}

@media (max-width: 1440px) {
  .example-section {
    font-size: 14px;
  }
}

@media (max-width: 1200px) {
  .example-section {
    padding: 1.2rem;
  }
  
  .experiment-section {
    padding: 1.2rem;
  }
}

@media (max-width: 768px) {
  .example-section {
    padding: 1rem;
    font-size: 13px;
  }

  .experiment-section {
    padding: 1rem;
    margin: 1rem 0;
  }

  .example-section h3 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
  }
  
  .experiment-section h4 {
    font-size: 1.1rem;
  }

  .color-picker {
    flex-direction: column;
  }
  
  .demo-box {
    padding: 0.8rem;
  }
  
  input[type="text"], input[type="number"] {
    padding: 0.6rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .example-section {
    padding: 0.8rem;
    font-size: 12px;
  }
  
  .experiment-section {
    padding: 0.8rem;
    margin: 0.8rem 0;
  }
  
  .demo-box {
    padding: 0.6rem;
  }
  
  .counter button {
    width: 32px;
    height: 32px;
    font-size: 1rem;
  }
  
  .color-box, input[type="color"] {
    width: 40px;
    height: 40px;
  }
}

/* Webkit 滚动条样式 (Chrome, Safari, Edge) */
.example-section::-webkit-scrollbar {
  width: 8px;
}

.example-section::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.example-section::-webkit-scrollbar-thumb {
  background-color: #d4d4d4;
  border-radius: 4px;
  border: 2px solid #f1f1f1;
}

.example-section::-webkit-scrollbar-thumb:hover {
  background-color: #aaa;
}

/* 实验描述样式 */
.experiment-desc {
  margin: 0.5rem 0 1rem 0;
  padding: 0.8rem 1rem;
  background-color: #edf7f2;
  border-radius: 6px;
  color: #3c6357;
  font-size: 0.95rem;
  line-height: 1.5;
  border-left: 3px solid #42b983;
}
</style> 