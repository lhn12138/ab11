import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import store from '../store';

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
                component: () => import('../views/analysis1.vue'),
                meta: {requiresAuth: true}
            },
            {
                path: '/analysis2',
                name: 'analysis2',
                component: () => import('../views/analysis2.vue'),
                meta: {requiresAuth: true}
            },
            {
                path: '/analysis3',
                name: 'analysis3',
                component: () => import('../views/analysis3.vue'),
                meta: {requiresAuth: true}
            }
        ]
    }]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes

})

router.beforeEach((to, from, next) => {
    const isLoggedIn = store.state.isLoggedIn;
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

    if (requiresAuth && !isLoggedIn) {
        next('/login');
    } else {
        next();
    }
});

export default router