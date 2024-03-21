import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
//     {
//         path: '/',
//         name: 'index',
//         redirect: '/a1',
//         component: () => import('../views/loginRegister.vue'),
// },
    {
        path: '/',
        name: 'index',
        redirect: '/analysis1',
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