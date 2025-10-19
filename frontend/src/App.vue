<script setup>
import { useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue';

const route = useRoute();

const showNav = () => {
  return route.name !== 'Login' && route.name !== 'Register';
}
</script>

<template>
  <div class="bg-slate-50">
    <NavBar v-if="showNav()" />
    <router-view />
  </div>
</template>