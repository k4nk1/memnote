<script setup>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <v-app>
    <Header />
    <v-main style="min-height: calc(100vh - 64px);">
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>