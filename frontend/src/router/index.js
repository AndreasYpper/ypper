import { createWebHistory, createRouter } from "vue-router";
import HomeView from '@/views/HomeView'
import ContactView from '@/views/ContactView'
import AboutView from '@/views/AboutView'
import ProjectsView from '@/views/ProjectsView'
import BlogView from '@/views/BlogView'

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
        path: '/about',
        name: 'about',
        component: AboutView
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
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;