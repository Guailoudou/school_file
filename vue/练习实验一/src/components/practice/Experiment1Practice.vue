<template>
  <div class="practice-section">
    <h2 class="main-title">练习区域</h2>
    
    <!-- 实验总体介绍 -->
    <section class="experiment-introduction">
      <h4>练习概述</h4>
      <div class="intro-content">
        <p>本练习区域提供了一系列与示例区域对应的实践任务，帮助您巩固所学的Vue 3基础知识。</p>
        <p>请尝试实现各种Vue指令、数据绑定和响应式特性，将理论知识转化为实际编码能力。</p>
        <p>每个练习都提供了明确的任务目标和基础代码结构，您需要完成剩余的实现部分。</p>
      </div>
    </section>
    
    <!-- 1. 单文件组件 -->
    <section class="experiment-section">
      <h3>1. 单文件组件</h3>
      <div class="experiment-desc">单文件组件是Vue应用的基本构建块，它将HTML模板、JavaScript逻辑和CSS样式封装在一个.vue文件中。本练习帮助您了解单文件组件的结构和组成部分。</div>
      <div class="content-box">
        <div class="description">
          <p>请查看实验区域左侧的单文件组件示例，无需完成</p>
        </div>
        <div class="practice-area">
          <div class="file-structure">
            <div class="file-part">
              <span class="file-label">template</span>
              <span>HTML结构</span>
            </div>
            <div class="file-part">
              <span class="file-label">script</span>
              <span>JavaScript逻辑</span>
            </div>
            <div class="file-part">
              <span class="file-label">style</span>
              <span>CSS样式</span>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 2. 数据绑定 -->
    <section class="experiment-section">
      <h3>2. 数据绑定</h3>
      <div class="experiment-desc">数据绑定是Vue的核心特性，使用插值表达式{{ }}可以轻松地将数据显示在模板中。本练习帮助您掌握基本的数据绑定和计算属性使用方法。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义message变量</li>
            <li>实现messageLength计算属性</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <input type="text" placeholder="输入消息">
            <p>消息：<span class="placeholder-text">在此显示message变量的值</span></p>
            <p>消息长度：<span class="placeholder-text">在此显示messageLength计算属性的值</span></p>
            <p class="directive-explanation">提示：使用ref创建响应式变量，使用computed创建计算属性，通过插值表达式{{message}}显示数据</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. 内容渲染指令 v-text 和 v-html -->
    <section class="experiment-section">
      <h3>3. 内容渲染指令</h3>
      <div class="experiment-desc">v-text和v-html指令可以将数据渲染到元素的内容中，区别在于v-html会解析HTML标签。本练习帮助您理解这两种指令的不同用途和适用场景。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义htmlContent变量</li>
            <li>使用v-text指令显示纯文本</li>
            <li>使用v-html指令渲染HTML内容</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-text指令</h4>
            <p class="placeholder-text">在这里使用v-text显示消息</p>
            
            <h4>v-html指令</h4>
            <input type="text" placeholder="输入HTML内容 (如: <b>粗体</b>)">
            <div class="html-preview placeholder-text">这里应显示HTML内容</div>
            <p class="directive-explanation">提示：v-text="message"会将数据作为纯文本显示，v-html="htmlContent"会解析HTML标签</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 属性绑定指令 v-bind -->
    <section class="experiment-section">
      <h3>4. 属性绑定指令</h3>
      <div class="experiment-desc">v-bind指令可以将Vue数据绑定到HTML属性上，使属性值随数据变化而动态更新。本练习帮助您掌握属性绑定以及class和style的动态绑定方法。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义link变量</li>
            <li>定义color变量</li>
            <li>定义isActive变量和toggleActive方法</li>
            <li>使用v-bind绑定href属性</li>
            <li>使用:style绑定样式</li>
            <li>使用:class绑定类</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-bind指令</h4>
            <input type="text" placeholder="输入链接地址">
            <div class="link-wrapper">
              <a href="#" target="_blank" class="placeholder-text">链接</a>
            </div>
            
            <h4>样式绑定</h4>
            <div class="color-picker">
              <input type="color">
              <div class="color-box placeholder-text"></div>
            </div>
            <p>当前颜色：<span class="placeholder-text">使用插值表达式显示颜色</span></p>
            
            <h4>class绑定</h4>
            <button class="placeholder-text">切换状态</button>
            <p class="directive-explanation">提示：v-bind:href可简写为:href，:style="{backgroundColor: color}"，:class="{ active: isActive }"</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. 双向绑定指令 v-model -->
    <section class="experiment-section">
      <h3>5. 双向绑定指令</h3>
      <div class="experiment-desc">v-model指令实现了表单元素与Vue数据的双向绑定，当数据变化时视图会更新，用户修改表单时数据也会同步更新。本练习帮助您掌握不同表单元素的双向绑定方法。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义inputText变量</li>
            <li>定义checked变量</li>
            <li>定义selected变量</li>
            <li>使用v-model分别绑定不同类型的表单元素</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-model 基本用法</h4>
            <input type="text" placeholder="输入文本">
            <p>输入的内容：<span class="placeholder-text">使用插值表达式显示输入内容</span></p>
            
            <h4>v-model 用于复选框</h4>
            <div class="checkbox-group">
              <label>
                <input type="checkbox"> 是否选中
              </label>
              <p>复选框状态：<span class="placeholder-text">使用插值表达式显示选中状态</span></p>
            </div>
            
            <h4>v-model 用于选择框</h4>
            <select>
              <option value="">请选择</option>
              <option value="A">选项A</option>
              <option value="B">选项B</option>
              <option value="C">选项C</option>
            </select>
            <p>当前选择：<span class="placeholder-text">使用插值表达式显示选择值</span></p>
            <p class="directive-explanation">提示：使用v-model="变量名"实现表单元素的双向数据绑定</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. 条件渲染指令 v-if 和 v-show -->
    <section class="experiment-section">
      <h3>6. 条件渲染指令</h3>
      <div class="experiment-desc">v-if和v-show都可以根据条件显示或隐藏元素，区别在于v-if会完全移除元素，而v-show只是切换display属性。本练习帮助您理解这两种条件渲染的使用场景。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义score变量</li>
            <li>定义loggedIn变量和username变量</li>
            <li>实现login和logout方法</li>
            <li>使用v-if/v-else-if/v-else根据分数显示不同级别</li>
            <li>使用v-show根据登录状态显示不同内容</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-if / v-else-if / v-else 指令</h4>
            <div class="score-input">
              <input type="number" placeholder="输入分数(0-100)">
            </div>
            <div class="result-display placeholder-text">
              <p>请完成条件渲染练习</p>
            </div>
            
            <h4>v-show 指令</h4>
            <div class="login-simulation">
              <div class="placeholder-text">
                <input type="text" placeholder="用户名">
                <button>登录</button>
              </div>
              <div class="placeholder-text">
                <p>欢迎回来！</p>
                <button>退出登录</button>
              </div>
            </div>
            <p class="directive-explanation">提示：v-if="condition"根据条件添加/移除元素，v-show="condition"根据条件切换display属性</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 列表渲染指令 v-for -->
    <section class="experiment-section">
      <h3>7. 列表渲染指令</h3>
      <div class="experiment-desc">v-for指令可以遍历数组或对象，为每个元素创建DOM元素。它是Vue中最强大的指令之一，可以渲染动态列表内容。本练习帮助您掌握列表渲染的基本用法和key的重要性。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义items数组</li>
            <li>定义newItem变量</li>
            <li>实现addItem和removeItem方法</li>
            <li>定义person对象</li>
            <li>使用v-for渲染数组和对象</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-for 基本用法</h4>
            <div class="list-controls">
              <input type="text" placeholder="添加项目">
              <button>添加</button>
            </div>
            <ul class="demo-list placeholder-text">
              <li>示例项目 <button class="delete-btn">删除</button></li>
            </ul>
            <p class="empty-list">完成列表渲染练习</p>
            
            <h4>v-for 与对象</h4>
            <ul class="demo-list placeholder-text">
              <li>请完成对象的列表渲染</li>
            </ul>
            <p class="directive-explanation">提示：v-for="(item, index) in items" :key="index"遍历数组，v-for="(value, key) in object" :key="key"遍历对象</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. 事件处理指令 v-on -->
    <section class="experiment-section">
      <h3>8. 事件处理指令</h3>
      <div class="experiment-desc">v-on指令可以监听DOM事件，并在事件触发时执行JavaScript代码。通过事件修饰符，可以更精细地控制事件处理行为。本练习帮助您掌握事件绑定和各种修饰符的使用。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义counter变量</li>
            <li>实现increment和decrement方法</li>
            <li>定义bubbleResult变量</li>
            <li>实现handleBubble和handleInner方法</li>
            <li>定义keyInput和keyResult变量</li>
            <li>实现submitInput方法</li>
            <li>使用v-on绑定各种事件和修饰符</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>v-on 基本用法</h4>
            <div class="counter">
              <button class="placeholder-text">-</button>
              <span class="placeholder-text">0</span>
              <button class="placeholder-text">+</button>
            </div>
            
            <h4>事件修饰符</h4>
            <div class="event-modifiers">
              <div class="bubble-container placeholder-text">
                <p>外层容器 (点击我)</p>
                <div class="bubble-inner">
                  <p>内层容器 (点击我，事件不会冒泡)</p>
                </div>
              </div>
              <p>事件触发：<span class="placeholder-text">显示事件触发结果</span></p>
            </div>
            
            <h4>按键修饰符</h4>
            <div class="key-modifiers">
              <input type="text" placeholder="输入文本并按Enter提交" class="placeholder-text">
              <p>提交结果：<span class="placeholder-text">显示提交结果</span></p>
            </div>
            <p class="directive-explanation">提示：v-on:click可简写为@click，使用.stop阻止事件冒泡，使用.enter监听Enter键</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. 计算属性 -->
    <section class="experiment-section">
      <h3>9. 计算属性</h3>
      <div class="experiment-desc">计算属性可以基于现有数据派生出新数据，并且会缓存结果直到依赖项变化。相比方法，计算属性在多次访问时具有更好的性能。本练习帮助您理解计算属性的优势和使用场景。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义number变量</li>
            <li>实现square计算属性</li>
            <li>实现cube计算属性</li>
            <li>实现isEven计算属性</li>
            <li>添加计算属性vs方法的对比</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <input type="number" placeholder="输入数字">
            <p>平方：<span class="placeholder-text">显示square计算属性</span></p>
            <p>立方：<span class="placeholder-text">显示cube计算属性</span></p>
            <p>是否偶数：<span class="placeholder-text">显示isEven计算属性</span></p>
            
            <h4>计算属性 vs 方法</h4>
            <p>计算属性会缓存，当依赖项不变时不会重新计算</p>
            <p>计算次数(计算属性)：<span class="placeholder-text">显示计算属性执行次数</span></p>
            <p>计算次数(方法)：<span class="placeholder-text">显示方法执行次数</span></p>
            <button>触发重新渲染</button>
            <p class="directive-explanation">提示：使用computed(() => { /* 计算逻辑 */ }) 创建计算属性</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 侦听器 -->
    <section class="experiment-section">
      <h3>10. 侦听器</h3>
      <div class="experiment-desc">侦听器可以监听数据变化并执行副作用操作，例如执行异步任务或复杂逻辑。当需要在数据变化时执行操作而不是派生新值时，侦听器是理想的选择。本练习帮助您掌握侦听器的基本用法。</div>
      <div class="content-box">
        <div class="description">
          <p>请实现：</p>
          <ul>
            <li>定义watchedValue变量</li>
            <li>定义watchCount变量</li>
            <li>定义watchHistory数组</li>
            <li>使用watch侦听变量变化并记录历史</li>
          </ul>
        </div>
        <div class="practice-area">
          <div class="directive-demo">
            <h4>侦听数据变化</h4>
            <input type="text" placeholder="修改此值会触发侦听器">
            <p>值变化次数：<span class="placeholder-text">显示watchCount值</span></p>
            <p>历史变化：</p>
            <ul class="history-list placeholder-text">
              <li>完成侦听器练习以查看历史记录</li>
            </ul>
            <p class="directive-explanation">提示：使用watch(variable, (newValue, oldValue) => { /* 执行操作 */ }) 创建侦听器</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
/*
 * 在此处实现练习区域所需的逻辑代码
 * 
 * 提示:
 * 1. 使用 ref 创建响应式变量
 * 2. 使用 computed 创建计算属性
 * 3. 使用 watch 创建侦听器
 * 4. 创建必要的方法处理事件
 */
</script>

<style scoped>
/* 基础布局样式 */
.practice-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  height: 100%;
  overflow-y: auto;
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

/* 标题样式 */
.main-title {
  color: #2c3e50;
  font-size: 1.8rem;
  text-align: center;
  margin-bottom: 2rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.main-title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #42b983, #2f9c69);
  border-radius: 2px;
}

/* 实验区块样式 */
.experiment-section {
  margin-bottom: 2.5rem;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  overflow: hidden;
}

.experiment-section h3 {
  background: #f8f8f8;
  color: #2c3e50;
  margin: 0;
  padding: 1rem;
  font-size: 1.4rem;
  border-bottom: 1px solid #e8e8e8;
}

.experiment-section h4 {
  color: #2c3e50;
  margin: 1rem 0 0.6rem;
  font-size: 1rem;
  border-left: 3px solid #42b983;
  padding-left: 0.8rem;
}

.content-box {
  padding: 1.5rem;
}

/* 描述区域样式 */
.description {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: #f8f8f8;
  border-radius: 6px;
  border-left: 4px solid #42b983;
}

.description p {
  margin: 0 0 0.5rem 0;
  color: #666;
  font-size: 0.9rem;
}

.description ul {
  margin: 0;
  padding-left: 1.2rem;
  color: #666;
  font-size: 0.9rem;
}

.description li {
  margin: 0.3rem 0;
}

/* 练习区域样式 */
.practice-area {
  margin-top: 1.5rem;
  padding: 1rem;
  border: 1px solid #eaeaea;
  border-radius: 6px;
  background-color: #fafafa;
}

/* 指令演示区域样式 */
.directive-demo {
  margin: 1rem 0 2rem;
  padding: 1.2rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e7e7e7;
}

.directive-explanation {
  margin-top: 0.8rem;
  font-size: 0.85rem;
  color: #666;
  font-style: italic;
  padding-left: 0.5rem;
  border-left: 2px solid #42b983;
}

/* 占位符文字样式 */
.placeholder-text {
  color: #999;
  border: 1px dashed #ccc;
  padding: 0.5rem;
  text-align: center;
  background-color: #f7f7f7;
  font-style: italic;
  display: inline-block;
  min-width: 100px;
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
  min-height: 50px;
  width: 100%;
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

.login-simulation div {
  margin: 0.5rem 0;
  padding: 0.5rem;
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
  min-height: 50px;
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
  margin: 1rem 0;
}

.counter button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background-color: #e9ecef;
  color: #2c3e50;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.counter button:hover {
  background-color: #dee2e6;
}

.counter span {
  min-width: 30px;
  text-align: center;
  font-size: 1.2rem;
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
  transform: translateY(-2px);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.checkbox-group {
  margin: 1rem 0;
}

/* 侦听器样式 */
.history-list {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
  min-height: 50px;
}

.history-list li {
  margin-bottom: 0.3rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .practice-section {
    padding: 1rem;
  }
  
  .main-title {
    font-size: 1.5rem;
  }
  
  h3 {
    font-size: 1.2rem;
  }
  
  .content-box {
    padding: 1rem;
  }
}
</style> 