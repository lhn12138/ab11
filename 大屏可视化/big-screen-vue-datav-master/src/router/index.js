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
        ]
    }]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes

})

export default router