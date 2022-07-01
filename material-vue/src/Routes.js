import Vue from 'vue';
import Router from 'vue-router';

import Layout from '@/components/Layout/Layout';

// Pages
import Dashboard from '@/pages/Dashboard/Dashboard';
import Typography from '@/pages/Typography/Typography'
import Tables from '@/pages/Tables/Basic'
import Notifications from '@/pages/Notifications/Notifications'
import Icons from '@/pages/Icons/Icons'
import Charts from '@/pages/Charts/Charts'
import Maps from '@/pages/Maps/Google'
import Error from "@/pages/Error/Error";
import Login from "@/pages/Login/Login";
import DailyCalorieIntake from "@/pages/DailyCalorieIntake/DailyCalorieIntake";
import BMI from "@/pages/BMI/BMI";
import IBW from "@/pages/IBW/IBW";
import CBC from "@/pages/CBC/CBC";
import Forget from "@/pages/Forget/Forget";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/forget',
      name: 'Forget',
      component: Forget
    },
    {
    path: '/',
    redirect: 'login',
    name: 'Layout',
    component: Layout,
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: Dashboard,
      },
      {
        path: 'typography',
        name: 'Typography',
        component: Typography,
      },
      {
        path: 'tables',
        name: 'Tables',
        component: Tables
      },
      {
        path: 'notifications',
        name: 'Notifications',
        component: Notifications
      },
      {
        path: 'icons',
        name: 'Icons',
        component: Icons
      },
      {
        path: 'charts',
        name: 'Charts',
        component: Charts
      },
      {
        path: 'maps',
        name: 'Maps',
        component: Maps
      },
      {
        path: 'dailycalorieintake',
        name: 'DailyCalorieIntake',
        component: DailyCalorieIntake
      },
      {
        path: 'bmi',
        name: 'BMI',
        component: BMI
      },
      {
        path: 'ibw',
        name: 'IBW',
        component: IBW
      },
      {
        path: 'cbc',
        name: 'CBC',
        component: CBC
      }
    ],
  },
    {
      path: '*',
      name: 'Error',
      component: Error
    }
  ],
});
