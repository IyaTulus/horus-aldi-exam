<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'
import api from '../services/api'

const router = useRouter()
const auth = useAuthStore()

const username = ref('')
const password = ref('')
const errorMessages = ref('')

const token = localStorage.getItem('token');
if (token !== null) {
    alert("Anda Sudah Login")
    router.push('/dashboard')
}

const handleLogin = async () => {
    errorMessages.value = '';

    if (!username.value || !password.value) {
        errorMessages.value = "Semua field wajib di isi!";
        return;
    }

    try {
        const res = await api.post('auth/login', {
            username: username.value,
            password: password.value
        })

        console.log('Response data:', res.data)
        auth.setAuth(res.data.access_token, res.data.user)

        alert('Login successful!')
        router.push('/dashboard')
    } catch (error) {
        errorMessages.value = "Login Gagal! Username atau password salah"
    }

}

const handelRemoveAlert = async () => {
    errorMessages.value = ''
}
</script>

<template>
    <main class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="h-[30rem] flex bg-white rounded shadow-md">
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
                    <h1 class="text-[#FF8400] font-bold text-2xl">Login</h1>
                    <p v-if="errorMessages" @click="handelRemoveAlert" class="text-sm text-red-500 cursor-pointer">
                        {{ errorMessages }}
                    </p>
                    <form @submit.prevent="handleLogin" method="POST" class="grid gap-5">

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
                            Login
                        </button>

                        <div class="text-center">
                            <p class="text-sm text-gray-600">
                                Tidak Memiliki Akun?
                                <router-link :to="{ name: 'Register' }"
                                    class="font-semibold text-[#FF8400] hover:underline">
                                    Daftar
                                </router-link>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</template>