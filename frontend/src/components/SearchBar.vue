<script setup>
import { ref } from 'vue';

const query = ref('');
const emit = defineEmits(['onSearch']);
const statusSearch= ref(false)

console.log(query);


const emitSearch = () => {
    emit('onSearch', query.value)
    if (query.value.length <= 0) {
        return
    }
    statusSearch.value = true
}

const deleteFilter = () => {
    statusSearch.value = false;
    query.value = ''
    emitSearch()
}
</script>

<template>
    <div class="flex items-center w-full max-w-sm p-3">
        <input v-model="query" type="text" placeholder="Cari Pengguna"
            class="flex-1 p-2 border border-gray-300 rounded-l-md outline-none focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
        <button @click="emitSearch"
            class="bg-[#FF8400] text-white px-4 py-2 rounded-r-md hover:bg-[#e67300] transition-all duration-200">
            Cari
        </button>
    </div>

    <div v-if="statusSearch" class="flex bg-green-100 px-5 py-2">
        <div class="w-full">
            <h1 class="text-slate-500">Cari: {{ query }}</h1>
        </div>
        <button @click="deleteFilter"
            class="flex items-center justify-center w-6 h-6 rounded-sm bg-green-500 text-white text-xs font-bold hover:bg-green-600 transition">
            ×
        </button>
    </div>
</template>