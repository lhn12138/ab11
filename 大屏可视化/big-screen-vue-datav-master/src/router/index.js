import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },

    {
        path: '/',
        name: 'index',
        redirect: '/login',
        component: () => import('../views/index.vue'),
        children: [
            {
                path: '/analysis1',
                name: 'analysis1',
                component: () => import('../views/analysis1.vue')
            },
            {
                path: '/analysis2',
                name: 'analysis2',
                component: () => import('../views/analysis2.vue')
            },
            {
                path: '/analysis3',
                name: 'analysis3',
                component: () => import('../views/analysis3.vue')
            }
        ],
        meta: { requiresAuth: true } // 添加此行,表示需要登录认证
    }]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes

})

// 添加以下代码,用于登录拦截
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated')
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})
export default router