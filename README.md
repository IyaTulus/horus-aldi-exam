```markdown
# 🐍 Flask REST API with MySQL, JWT Authentication & Blueprint

## 📘 Deskripsi
Proyek ini adalah RESTful API menggunakan **Flask** dengan **MySQL (phpMyAdmin)** sebagai database.  
Struktur proyek mengikuti pola **Blueprint** agar modular dan mudah dikembangkan.  
API ini mencakup fitur:
- Registrasi dan login user
- Autentikasi menggunakan **JWT**
- Proteksi endpoint (hanya user yang login bisa akses)
- Fitur **search** dan **delete user**
- CORS support untuk koneksi dari frontend (React, Vue, dll)

---
```


## ⚙️ Instalasi & Konfigurasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/IyaTulus/horus-aldi-exam
````

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Konfigurasi Database

Edit file `app/config.py`:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/nama_database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "supersecretkey"
```

> Pastikan database `nama_database` sudah dibuat di phpMyAdmin.

### 5️⃣ Migrasi Database

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6️⃣ Jalankan Server

```bash
python run.py
```

API akan berjalan di:

```
http://127.0.0.1:5000/
```

---

## 🔑 Endpoint API

### 🧍‍♂️ Register User

**POST** `/users/register`

**Request Body:**

```json
{
    "nama": "Aldi",
    "username": "aldidev",
    "email": "aldi@example.com",
    "password": "password123"
}
```

**Response:**

```json
{
    "id": 1,
    "nama": "Aldi",
    "username": "aldidev",
    "email": "aldi@example.com",
    "created_at": "2025-10-18T10:00:00"
}
```

---

### 🔐 Login User

**POST** `/auth/login`

**Request Body:**

```json
{
    "username": "aldi@example.com",
    "password": "password123"
}
```

**Response:**

```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJI..."
}
```

---
### ❌ Delete User (Protected)

**DELETE** `/users/delete/<int:id>`

**Headers:**

```
Authorization: Bearer <JWT_TOKEN>
```

**Response:**

```json
{
    "message": "User berhasil dihapus"
}
```
---

## 📦 Dependencies

Contoh isi `requirements.txt`:

```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.7
Flask-JWT-Extended==4.6.0
Flask-Cors==4.0.1
PyMySQL==1.1.1
python-dotenv==1.0.1
```

---

Berikut format **README.md** lengkap untuk instalasi dan menjalankan **frontend Vue 3 + Vite + Tailwind + Axios** (seperti proyek kamu):

---

````md
# 🚀 Horus Exam Frontend

Frontend dari aplikasi **Horus Exam**, dibangun menggunakan **Vue 3 (Composition API)**, **Vite**, dan **Tailwind CSS**.  
Aplikasi ini berfungsi sebagai dashboard admin untuk mengelola data pengguna, autentikasi, serta profil pengguna.

---

## 🧩 Teknologi yang Digunakan
- [Vue 3](https://vuejs.org/) (Composition API)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)
- [Vue Router](https://router.vuejs.org/)
- [Pinia](https://pinia.vuejs.org/) (State Management)

---

## ⚙️ Persiapan Awal

### 1. Clone Repository
```bash
git clone https://github.com/IyaTulus/horus-aldi-exam
````

### 2. Install Dependencies

Gunakan **npm** atau **yarn**:

```bash
npm install
```

atau

```bash
yarn install
```

---

## ⚡️ Menjalankan Project

### 1. Jalankan Server Development

```bash
npm run dev
```

Secara default akan berjalan di:

```
http://localhost:5173
```

---

## 🔧 Konfigurasi Environment

Buat file `.env` di root project dengan isi berikut:

```bash
VITE_API_BASE_URL=http://127.0.0.1:5000
```

> Pastikan backend Flask sudah berjalan di alamat tersebut.

---

## 📁 Struktur Folder

```
src/
├── assets/              # File static seperti gambar/icon
├── components/          # Komponen UI (Navbar, SearchBar, UserTable, dll)
├── services/            # Konfigurasi Axios API
│   └── api.js
├── store/               # Store Pinia (auth, user)
├── views/               # Halaman (Login, Register, Dashboard, Profile, UpdateUser)
├── router/              # Routing aplikasi
│   └── index.js
└── main.js              # Entry utama aplikasi
```

---

## 🔒 Autentikasi

* Token JWT disimpan di **localStorage**
* Interceptor Axios otomatis menambahkan header:

  ```
  Authorization: Bearer <token>
  ```
* Logout akan menghapus token dan redirect ke halaman login

---

## 🧪 Build untuk Production

```bash
npm run build
```

Hasil build akan tersimpan di folder `dist/`.

Untuk menjalankan hasil build secara lokal:

```bash
npm run preview
```

---


## 👨‍💻 Pengembang

**Aldi Tulus Pribadi**
Universitas Ahmad Dahlan

---

## 📜 Lisensi


---



