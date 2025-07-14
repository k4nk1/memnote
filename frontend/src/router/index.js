import { createRouter, createWebHistory } from 'vue-router';
import Index from '../pages/Index.vue';
import NewNote from '../pages/newNote.vue';
import MyNotes from '../pages/MyNotes.vue';
import Edit from '../pages/Edit.vue';
import Memorize from '../pages/Memorize.vue';

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
    },
    {
        path: '/notes/:nid/edit',
        name: 'Edit',
        component: Edit
    },
    {
        path: '/notes/:nid/memorize',
        name: 'Memorize',
        component: Memorize
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;