<script setup>
import api from '@/services/api'
import { useAuthStore } from '@/store/auth'
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()
const token = localStorage.getItem('token');
if (token === null) {
    alert("Anda Belum Login")
    router.push('/')
}

const nama = ref('')
const username = ref('')
const email = ref('')
const created_at = ref('')


onMounted(async () => {
    try {
        const res = await api.get('/auth/me')
        console.log('Response full:', res.data)

        const data = res.data.user

        nama.value = data.nama
        username.value = data.username
        email.value = data.email
        created_at.value = data.created_at

        console.log('Data user berhasil dimuat:', data)
    } catch (error) {
        console.error('Gagal memuat profil:', error.response?.data || error.message)
    }
})

const formatDate = (dateStr) => {
    const date = new Date(dateStr)
    return date.toLocaleDateString('id-ID', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
    })
}

const goBack = () => {
    router.push('/dashboard')
}


const handleLogout = async () => {
    try {
        const res = await api.post('auth/logout');

        console.log('response : ', res.data);
        auth.clearAuth();
        alert("anda Berhasil logout")
        router.push('/')
    } catch (error) {
        console.log(error);
    }
}
</script>

<template>
    <div class="px-3 sm:px-[10rem] pt-[5rem]">
        <div class="bg-gray-50 p-6 flex">
            <div class="bg-white rounded-sm shadow-md w-full">
                <div class="p-6">

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                        <div>
                            <label class="block text-sm font-medium text-slate-500 mb-1">Nama Lengkap</label>
                            <div class="border border-gray-300 rounded-md px-3 py-2 text-slate-800 bg-gray-50">
                                {{ nama }}
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-slate-500 mb-1">Username</label>
                            <div class="border border-gray-300 rounded-md px-3 py-2 text-slate-800 bg-gray-50">
                                {{ username }}
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-slate-500 mb-1">Email</label>
                            <div class="border border-gray-300 rounded-md px-3 py-2 text-slate-800 bg-gray-50">
                                {{ email }}
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-slate-500 mb-1">Dibuat Pada</label>
                            <div class="border border-gray-300 rounded-md px-3 py-2 text-slate-800 bg-gray-50">
                                {{ formatDate(created_at) }}
                            </div>
                        </div>
                    </div>

                    <div class="mt-8 flex justify-end space-x-3">
                        <button @click="goBack"
                            class="px-4 py-2 border border-gray-300 rounded-md text-slate-600 hover:bg-gray-100 transition-all">
                            Kembali
                        </button>
                        <button @click="handleLogout"
                            class="px-4 py-2 bg-[#FF8400] text-white rounded-md hover:bg-[#e67300] transition-all">
                            Logout
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>