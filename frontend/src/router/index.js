import { createRouter, createWebHistory } from 'vue-router';
import Index from '../components/Index.vue';
import NewNote from '../components/newNote.vue';
import MyNotes from '../components/MyNotes.vue';

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
    },
    {
        path: '/mynotes',
        name: 'MyNotes',
        component: MyNotes
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;