import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import {isLoggedIn} from '@/utils/auth';

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
        meta: {auth: true},
        children: [
            {
                path: '/analysis1',
                name: 'analysis1',
                component: () => import('../views/analysis1.vue'),
                meta: {auth: true}
            },
            {
                path: '/analysis2',
                name: 'analysis2',
                component: () => import('../views/analysis2.vue'),
                meta: {auth: true}
            },
            {
                path: '/analysis3',
                name: 'analysis3',
                component: () => import('../views/analysis3.vue'),
                meta: {auth: true}
            }
        ]
    }]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes

})
router.beforeEach((to, from, next) => {
    // 检查是否需要登录验证
    if (to.meta.auth) {
        // 检查用户是否登录
        if (!isLoggedIn()) {
            // 未登录,跳转到登录页面
            console.log('User is not logged in, redirecting to login page');
            next('/login');
        } else {
            // 已登录,放行
            console.log('User is logged in, allowing access to protected route');
            next();
        }
    } else {
        // 不需要登录验证,放行
        next();
    }
});
export default router