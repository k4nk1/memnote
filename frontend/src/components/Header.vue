<template>
    <v-app-bar>
        <v-app-bar-title>
            <router-link class="app-bar-link" to="/">
                <img class="app-bar-logo" src="../assets/memnote.svg">
            </router-link>
        </v-app-bar-title>
        <router-link class="app-bar-link" to="/newnote">新規ノート</router-link>
        <router-link class="app-bar-link" to="/mynotes">マイノート</router-link>
    </v-app-bar>
</template>

<style scoped>
.v-app-bar-title{
    height: 100%;
    margin-left: 0;
    align-self: center;
    font-size: 2.2rem;
}
.v-toolbar-title{
    height: 64px;
}
.app-bar-link{
    color: black;
    text-decoration: none;
    font-weight: bold;
    padding: 20px 0.5vw 20px 0.5vw;
    margin: 0 0.5vw;
}
.app-bar-logo{
    max-width: calc(100vw - 180px);
    max-height: 64px;
    padding: 10px 1vw;
    margin: auto 0;
}
</style>