import { createRouter, createWebHistory } from 'vue-router'
import Experiment2 from '../views/Experiment2.vue'

const routes = [
  {
    path: '/',
    redirect: '/experiment2'
  },
  {
    path: '/experiment2',
    name: 'Experiment2',
    component: Experiment2
  },
  {
    path: '/experiment3',
    name: 'Experiment3',
    component: () => import('../views/Experiment3.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 