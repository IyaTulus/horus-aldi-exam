<script setup>
import api from '@/services/api'
import { computed, onMounted, ref } from 'vue'
import SearchBar from './SearchBar.vue';
import router from '@/routes';

const props = defineProps({
    searchQuery: {
        type: String, default: ''
    }
})

const users = ref([])

onMounted(async () => {
    try {
        const res = await api.get('users/data');
        users.value = res.data.items;
    } catch (error) {
        console.error(error);
    }
})

const filterUser = computed(() => {
    if (!props.searchQuery) {
        return users.value   
    }
    return users.value.filter(u => 
        u.nama.toLowerCase().includes(props.searchQuery.toLowerCase()) ||
        u.email.toLowerCase().includes(props.searchQuery.toLowerCase()) ||
        u.username.toLowerCase().includes(props.searchQuery.toLowerCase())
    )
})

console.log("data filter" + JSON.stringify(filterUser.value));

const editUser = (user) => {
    router.push({
        name: "UpdateUser",
        query: {
            id: user.id
        }
    })
}

const deleteUser = async(id) => {
    if (confirm('Yakin ingin menghapus user ini?')) {
        users.value = users.value.filter((u) => u.id !== id)
        await api.delete(`/users/${id}`)
    }
}
</script>

<template>
    <div class="overflow-x-auto">
        <table class="min-w-full border border-gray-200">
            <thead class="bg-slate-200">
                <tr class="text-left text-gray-600">
                    <th class="py-3 px-4 border-b">No</th>
                    <th class="py-3 px-4 border-b">Nama</th>
                    <th class="py-3 px-4 border-b">Username</th>
                    <th class="py-3 px-4 border-b">Email</th>
                    <th class="py-3 px-4 border-b text-center">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(user, index) in filterUser" :key="user.id" class="hover:bg-gray-50 transition duration-200">
                    <td class="py-3 px-4 border-b">{{ index + 1 }}</td>
                    <td class="py-3 px-4 border-b font-medium text-gray-700">{{ user.nama }}</td>
                    <td class="py-3 px-4 border-b font-medium text-gray-700">{{ user.username }}</td>
                    <td class="py-3 px-4 border-b text-gray-600">{{ user.email }}</td>
                    <td class="py-3 px-4 border-b text-center">
                        <button @click="editUser(user)" class="text-blue-500 hover:text-blue-700 mx-1"
                            title="Edit User">
                            Edit
                        </button>
                        <button @click="deleteUser(user.id)" class="text-red-500 hover:text-red-700 mx-1"
                            title="Delete User">
                            Hapus
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
table {
    border-collapse: separate;
    border-spacing: 0;
}
</style>
