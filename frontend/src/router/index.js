import { createWebHistory, createRouter } from "vue-router";

import HomeView from '@/views/ypper/HomeView'

// import AuthenticationView from '@/views/authentication/AuthenticationView'

// import ProfileView from '@/views/user/ProfileView'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;