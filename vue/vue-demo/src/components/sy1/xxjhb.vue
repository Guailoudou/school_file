<script setup>
import { ref } from 'vue'
const list = ref([
  {
    id: '1',
    subject: 'Vue.js 前端实战开发',
    content: '学习指令，例如 v-if、v-for、v-model 等',
    place: '自习室',
    status: false,
  },
]);
let remove = (id, status) => {
  if (status) {
    list.value = list.value.filter(item => item.id !== id)
  } else {
    alert('请完成该学习计划后再进行删除操作！')
  }
}
let subject = ref('')
let content = ref('')
let nextId = ref('')
let selectedOption = ref('自习室')
let options = ref([
  { placeCode: 0, place: '自习室', },
  { placeCode: 1, place: '图书馆', },
  { placeCode: 2, place: '宿舍', },
])

let add = () => {
  if (subject.value === '') {
    alert('学习科目为必填项！')
    return
  }
  nextId.value = Math.max(...list.value.map(item => item.id)) + 1
  const obj = {
    id: nextId.value,
    subject: subject.value,
    content: content.value,
    place: selectedOption.value,
    status: false,
  }
  list.value.push(obj)
  subject.value = ''
  content.value = ''
  selectedOption.value = '自习室'
}

</script>
<template>
  <div class="card">
    <!-- 标题区域 -->
    <div class="card-header">学习计划表</div>
    <!-- 提交区域 -->
    <div class="card-body">
      <form @submit.prevent="add">
        <div class="row g-4">
          <div class="col-auto">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">学习科目</span>
              <input type="text" class="form-control" placeholder="请输入学习科目" v-model.trim="subject" />
            </div>
          </div>

          <div class="col-auto"></div>
          <div class="col-auto">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">学习内容</span>
              <textarea class="form-control" v-model.trim="content" placeholder="请输入学习内容"
                :style="{ height: '32px' }"></textarea>
            </div>
          </div>

          <div class="col-auto"></div>
          <div class="col-auto">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">学习地点</span>
              <select class="form-select form-select-sm" v-model="selectedOption">
                <option v-for="option in options" :value="option.place" :key="option.placeCode">
                  {{ option.place }}
                </option>
              </select>
            </div>
          </div>

          <div class="col-auto"></div>
          <!-- 添加按钮 -->
          <div class="col-auto">
            <button type="submit" class="btn btn-primary">添加</button>
          </div>
        </div>
      </form>
    </div>
  </div>
  <table class="table table-striped table-hover table-bordered">
    <thead>
      <tr>
        <th scope="col">序号</th>
        <th scope="col">学习科目</th>
        <th scope="col">学习内容</th>
        <th scope="col">学习地点</th>
        <th scope="col">完成状态</th>
        <th scope="col">操作</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in list" :key="item.id">
        <td>{{ index + 1 }}</td>
        <td>{{ item.subject }}</td>
        <td>{{ item.content }}</td>
        <td>{{ item.place }}</td>
        <td>
          <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" :id="'cb' + item.id" v-model="item.status" />
            <label class="form-check-label" :for="'cb' + item.id" v-if="item.status">已完成</label>
            <label class="form-check-label" :for="'cb' + item.id" v-else>未完成</label>
          </div>

        </td>
        <td>
          <a href="javascript:;" @click="remove(item.id, item.status)">删除</a>
        </td>
      </tr>
    </tbody>

  </table>
</template>