<script setup>
import router from '@/routes';
import api from '@/services/api';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const token = localStorage.getItem('token');
if (token === null) {
    alert("Anda Belum Login")
    router.push('/')
}

const dataUser = ref('');
const dataId = route.query.id;
const nama = ref('')
const email = ref('')
const username = ref('')
const errorMessages = ref('')

onMounted(async () => {
    const res = await api.get(`/users/${dataId}`);
    dataUser.value = res.data;

    nama.value = dataUser.value.nama;
    email.value = dataUser.value.email
    username.value = dataUser.value.username
})

const isValidEmail = (email) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)
}

const handleUpdate = async () => {
    errorMessages.value = '';

    if (!username.value || !nama.value || !email.value) {
        errorMessages.value = "Semua field wajib di isi!";
        return;
    }

    if (!isValidEmail(email.value)) {
        errorMessages.value = "Format email tidak valid!";
        return;
    }

    const res = await api.put(`/users/${dataId}`, {
        nama: nama.value,
        email: email.value,
        username: username.value,
    })

    console.log('Response data:', res.data)

    alert('Berhasil Di Ubah!')
    router.push('/dashboard')

}

</script>

<template>
    <div class="px-3 sm:px-[10rem] pt-[5rem]">
        <main class="flex flex-col space-y-6">
            <h1 class="text-2xl text-slate-600">Edit User</h1>
            <div class="mb-10">
                <div class="bg-white rounded-sm shadow-md p-4 mb-6">
                    <p v-if="errorMessages" @click="handelRemoveAlert" class="text-sm text-red-500 cursor-pointer">
                        {{ errorMessages }}
                    </p>
                    <form class="space-y-6">
                        <div>
                            <label class="block text-sm font-medium text-slate-600 mb-2">
                                Nama Lengkap
                            </label>
                            <input v-model="nama" type="text" placeholder="Masukkan nama lengkap"
                                value="{{ dataUser.nama }}"
                                class="w-full border border-gray-300 rounded-lg p-3 text-slate-700 focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-slate-600 mb-2">
                                Username
                            </label>
                            <input v-model="username" type="text" placeholder="Masukkan username"
                                class="w-full border border-gray-300 rounded-lg p-3 text-slate-700 focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-slate-600 mb-2">
                                Email
                            </label>
                            <input v-model="email" type="email" placeholder="Masukkan email pengguna"
                                class="w-full border border-gray-300 rounded-lg p-3 text-slate-700 focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>
                        <div class="flex justify-end space-x-3 pt-4">
                            <router-link :to="{ name: 'Dashboard' }" type="button"
                                class="bg-gray-300 text-gray-700 px-5 py-2 rounded-lg hover:bg-gray-400 transition-all">Batal</router-link>
                            <button type="button" @click="handleUpdate"
                                class="bg-[#FF8400] text-white px-5 py-2 rounded-lg hover:bg-[#e67300] transition-all">
                                Simpan Perubahan
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </main>
    </div>
</template>