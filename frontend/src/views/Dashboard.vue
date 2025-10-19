<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'
import api from '../services/api'
import UserTable from '@/components/UserTable.vue';
import { ref } from 'vue';
import SearchBar from '@/components/SearchBar.vue';

const auth = useAuthStore()
const router = useRouter();
const token = localStorage.getItem('token');
if (token === null) {
    alert("Anda Belum Login")
    router.push('/')
}


const searchQuery = ref('');
const handleSearch = (query) => {
    searchQuery.value = query
}
</script>

<template>
    <div class="px-3 sm:px-[10rem] pt-[5rem]">
        <main class="flex flex-col space-y-6">
            <h1 class="text-2xl text-slate-600">Data User</h1>
            <div class="mb-10">
                <div class="bg-white rounded-sm shadow-md">
                    <SearchBar @onSearch = "handleSearch" class="p-6"/>
                    <UserTable :searchQuery="searchQuery" class="mb-[3rem]"/>
                </div>
            </div>
        </main>
    </div>
</template>