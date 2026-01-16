# 📝 Django Todo App

Aplikasi Todo sederhana yang dibuat menggunakan Django.  
Proyek ini dibuat sebagai contoh portofolio backend dengan fokus pada fitur CRUD dan struktur project yang rapi.

---

## 🚀 Fitur Utama
- Tambah tugas
- Edit tugas
- Hapus tugas
- Tandai tugas selesai / belum
- Tampilan simpel menggunakan Bootstrap

---

## 🛠 Teknologi yang Digunakan
- **Python 3**
- **Django**
- **SQLite** (default Django)
- **HTML + Bootstrap** untuk tampilan dasar

---

## ▶️ Cara Menjalankan di Lokal

### 1. Clone repository
```bash
git clone https://github.com/adityasuryaj/django-todo-app.git
```

### 2. Masuk ke direktori project
```bash
cd django-todo-app
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Migrasi database
```bash
python manage.py migrate
```

### 5. Jalankan server
```bash
python manage.py runserver
```

Aplikasi dapat diakses di:  
http://127.0.0.1:8000/

---

## 📁 Struktur Singkat Project
```
todo_project/
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
└── manage.py
```

---

## 📄 Tujuan Project
Project ini dibuat sebagai latihan dasar Django dan contoh sederhana kemampuan backend development:

- Mengelola model dan database  
- Mengatur routing & view  
- Membuat form dan proses CRUD  
- Memahami dasar template Django  

---

## 🧑‍💻 Status
Proyek ini bersifat sederhana dan ditujukan untuk portofolio awal.  
Fitur dapat dikembangkan lebih lanjut di masa depan.
