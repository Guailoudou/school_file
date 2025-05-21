import { RouterView, createRouter, createWebHashHistory } from 'vue-router'
import { h } from 'vue'

const router = createRouter({
    history: createWebHashHistory(), routes: [
        { path: '/', redirect: '/login' },
        { path: '/login', component: () => import('./components/Login.vue') },
        {
            path: '/home',
            component: () => import('./components/Home.vue'),
            redirect: '/home/users',

            children: [
                {
                    path: 'users',
                    component: { render: () => h(RouterView) }, children: [
                        {
                            path: '',
                            component: () => import('./components/subcomponents/MyUsers.vue')
                        },
                        {
                            path: ':id',
                            name: 'details',
                            component: () => import('./components/user/MyUserDetail.vue'), props: true
                        },
                        {
                            path: 'rights',
                            component: () => import('./components/subcomponents/MyRights.vue')
                        },
                        {
                            path: 'goods',
                            component: () => import('./components/subcomponents/MyGoods.vue')
                        },
                        {
                            path: 'orders',
                            component: () => import('./components/subcomponents/MyOrders.vue')
                        },
                        {
                            path: 'settings',
                            component: () => import('./components/subcomponents/MySettings.vue')
                        },
                        {
                            path: 'menu',
                            component: () => import('./components/subcomponents/MyMenu.vue')

                        }

                    ]
                }]
        }]
})
export default router



router.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        return next()
    }
    const token = localStorage.getItem('token')
    if (!token) {
        return next('/login')
    }
    next()
})

