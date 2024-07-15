import { createRouter, createWebHistory } from 'vue-router';
import Index from '../components/Index.vue';
import NewNote from '../components/newNote.vue';

const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index
    },
    {
        path: '/newnote',
        name: 'NewNote',
        component: NewNote
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;