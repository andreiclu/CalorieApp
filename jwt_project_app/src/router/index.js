import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from "@/views/SignUp";
import Login from "@/views/Login";
import Search from "@/views/Search";
import Meals from "@/views/Meals";
import BMICalculator from "@/views/BMICalculator";
import IdealBodyWeight from "@/views/IdealBodyWeight";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/search',
        name: 'search',
        component: Search
    },
    {
        path: '/about',
        name: 'about',
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/meals',
        name: 'Meals',
        component: Meals
    },
    {
        path: '/log-in',
        name: 'Login',
        component: Login
    },
    {
        path: '/bmicalculator',
        name: 'bmicalculator',
        component: BMICalculator
    },
    {
        path: '/idealbodyweight',
        name: 'idealbodyweight',
        component: IdealBodyWeight
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
