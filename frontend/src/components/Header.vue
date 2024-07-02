<script setup>
import { ref } from 'vue';
const has_id = ref(true);
</script>

<template>
    <v-app-bar>
        <v-app-bar-title>
            <router-link class="app-bar-link" style="width: 5.5em;" to="/">
                memnote
            </router-link>
        </v-app-bar-title>
        <router-link class="app-bar-link" to="/notes/new">新規ノート</router-link>
        <template v-if="has_id">
            <router-link class="app-bar-link" to="/mynotes">マイノート</router-link>
        </template>
    </v-app-bar>
</template>

<style scoped>
.v-app-bar-title{
    height: 100%;
    align-self: center;
    font-size: 2.2rem;
}
.app-bar-link{
    display: flex;
    color: black;
    text-decoration: none;
    font-weight: bold;
    padding: 20px 5px 20px 5px;
    margin: 0 10px 0 10px;
}
</style>