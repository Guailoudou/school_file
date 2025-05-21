import { createRouter, createWebHistory } from 'vue-router'
import Experiment1 from '../views/Experiment1.vue'

const routes = [
  {
    path: '/',
    redirect: '/experiment1'
  },
  {
    path: '/experiment1',
    name: 'Experiment1',
    component: Experiment1
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 