<script setup>
import { ref } from 'vue'

const menuStatus = ref(false)

const menuToggle = () => {
  menuStatus.value = !menuStatus.value
}

</script>

<template>
    <header
        class="fixed top-0 bg-white/30 w-full px-3 sm:px-[12rem] backdrop-blur-sm bg-white text-[#FF8400] z-50">
        <div class="flex justify-between items-center w-full py-4">
            <div>
                <h1 class="text-2xl font-bold">Horus Exam</h1>
            </div>
            <div class="hidden sm:block">
                <ul class="flex space-x-10 text-slate-400">
                    <li class="p-1 rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                        <router-link to="/dashboard">Dashboard</router-link>
                    </li>
                    <li class="p-1 rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                        <router-link to="#">User Data</router-link>
                    </li>
                    <li class="p-1 rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                        <router-link to="#">About</router-link>
                    </li>
                </ul>
            </div>
            <div class="hidden sm:block">
                <router-link :to="{ name: 'Profile' }" class="bg-red-100 px-4 py-2 rounded-md">Profile</router-link>
            </div>
            <div class="sm:hidden block">
                <button @click="menuToggle" class="bg-red-100 px-4 py-2 rounded-md">Menu</button>
            </div>
        </div>
    </header>
    <div v-if="menuStatus" class="fixed sm:hidden mt-[5rem] bg-slate-200 flex flex-col justify-between items-center w-full py-4 duration-300 ease-in-out">
        <ul class="flex flex-col w-full items-center justify-center text-slate-400 text-center">
            <li class="p-1 w-full rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                <router-link to="/dashboard">Dashboard</router-link>
            </li>
            <li class="p-1 w-full rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                <router-link to="#">User Data</router-link>
            </li>
            <li class="p-1 w-full rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                <router-link to="#">About</router-link>
            </li>
            <li class="p-1 w-full rounded-sm hover:bg-slate-100 hover:text-slate-500 duration-300 ease-in-out">
                <router-link to="#">Profile</router-link>
            </li>
        </ul>
    </div>
</template>