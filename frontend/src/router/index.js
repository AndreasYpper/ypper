import { createWebHistory, createRouter } from "vue-router";

import HomeView from '@/views/ypper/HomeView'
import ContactView from '@/views/ypper/ContactView'
import ProjectsView from '@/views/ypper/ProjectsView'
import BlogView from '@/views/ypper/BlogView'

import MachineHomeView from '@/views/machine_news/MachineHomeView'

import AuthenticationView from '@/views/authentication/AuthenticationView'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/contact',
        name: 'contact',
        component: ContactView
    },
    {
        path: '/projects',
        name: 'projects',
        component: ProjectsView
    },
    {
        path: '/blog',
        name: 'blog',
        component: BlogView
    },
    {
        path: '/machine_news',
        name: 'machine_news_home',
        component: MachineHomeView
    },
    {
        path: '/auth',
        name: 'authentication',
        component: AuthenticationView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;