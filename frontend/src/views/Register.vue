<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'
import api from '../services/api'

const router = useRouter()
const auth = useAuthStore()

const nama = ref('')
const email = ref('')
const username = ref('')
const password = ref('')
const errorMessages = ref('')

const token = localStorage.getItem('token');

if (token !== null) {
    alert("Anda Sudah Login")
    router.push('/dashboard')
}

const isValidEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return regex.test(email)
}

const handleRegister = async () => {
    errorMessages.value = '';

    if (!username.value || !password.value) {
        errorMessages.value = "Semua field wajib di isi!";
        return;
    }

    if (password.value.length < 6) {
        errorMessages.value = "Semua field wajib di isi!";
        return;
    }

    if (!isValidEmail(email.value)) {
        errorMessages.value = "Format email tidak valid!";
        return;
    }

    try {
        const res = await api.post('/users/register', {
            nama: nama.value,
            email: email.value,
            username: username.value,
            password: password.value
        })

        console.log('Response data:', res.data)

        alert('Register successful!')
        router.back('/login')
    } catch (error) {
        errorMessages.value = "Register Gagal! Username atau email sudah ada"
    }
}

const handelRemoveAlert = async () => {
    errorMessages.value = ''
}
</script>

<template>
    <main class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="h-[38rem] flex bg-white rounded shadow-md">
            <div class="hidden sm:block w-[35rem] bg-gradient-to-bl from-[#FF8400] to-[#FFD93D] border-r text-white p-12">
                <h1 class="text-6xl font-bold">
                    Welcome to Website
                </h1>
                <p class="mt-4 text-lg text-yellow-100/90">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore
                    et dolore magna aliqua.
                </p>

            </div>
            <div class="w-[20rem] sm:w-[25rem] flex items-center justify-center border-r p-12">
                <div class="w-full grid grid-flow-row gap-4">
                    <h1 class="text-[#FF8400] font-bold text-2xl">Daftar Akun</h1>
                    <p v-if="errorMessages" @click="handelRemoveAlert" class="text-sm text-red-500 cursor-pointer">
                        {{ errorMessages }}
                    </p>
                    <form @submit.prevent="handleRegister" method="POST" class="grid gap-5">

                        <div class="grid gap-2">
                            <label for="nama" class="font-semibold text-gray-700">Nama Lengkap</label>
                            <input type="text" v-model="nama" placeholder="Nama Lengkap"
                                class="w-full p-3 border border-gray-300 rounded-md outline-none focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>

                        <div class="grid gap-2">
                            <label for="email" class="font-semibold text-gray-700">Email</label>
                            <input type="text" v-model="email" placeholder="Email Lengkap"
                                class="w-full p-3 border border-gray-300 rounded-md outline-none focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>

                        <div class="grid gap-2">
                            <label for="username" class="font-semibold text-gray-700">Username</label>
                            <input type="text" v-model="username" placeholder="username"
                                class="w-full p-3 border border-gray-300 rounded-md outline-none focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>

                        <div class="grid gap-2">
                            <label for="password" class="font-semibold text-gray-700">Password</label>
                            <input type="password" v-model="password" placeholder="••••••••"
                                class="w-full p-3 border border-gray-300 rounded-md outline-none focus:ring-2 focus:ring-[#FF8400] focus:border-transparent transition-all duration-200" />
                        </div>

                        <button type="submit"
                            class="w-full bg-[#FF8400] text-white font-bold py-3 rounded-md hover:bg-[#E07300] transition-colors duration-200">
                            Daftar
                        </button>

                        <div class="text-center">
                            <p class="text-sm text-gray-600">
                                Sudah Memiliki Akun?
                                <router-link :to="{ name: 'Login' }"
                                    class="font-semibold text-[#FF8400] hover:underline">
                                    Login
                                </router-link>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</template>