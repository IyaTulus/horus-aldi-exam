import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";
import Register from "@/views/Register.vue";
import UpdateUser from "@/views/UpdateUser.vue";
import Profile from "@/views/Profile.vue";

const routes = [
    { path: "/", name: "Login", component: Login},
    { path: "/register", name: "Register", component: Register},
    { path: "/dashboard", name: "Dashboard", component: Dashboard},
    { path: "/update", name: "UpdateUser", component: UpdateUser},
    { path: "/profile", name: "Profile", component: Profile}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;