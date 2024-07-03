<script setup>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <v-app>
    <Header />
    <v-main style="min-height: 100vh;">
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>