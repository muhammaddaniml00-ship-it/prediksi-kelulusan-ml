# 🎓 Belajar Machine Learning: Prediksi Kelulusan Ujian

Project ini dibuat untuk **pemula yang baru mulai belajar Machine Learning**,
khususnya yang **mau dipresentasikan**. Semua penjelasan dalam Bahasa Indonesia.

---

## ⭐ Project utama (gampang di-presentasikan)

**Prediksi Kelulusan Ujian** — pakai algoritma **KNN**.

> "Kita punya data siswa lama (jam belajar, jam tidur, lulus/tidak).
> Datang siswa baru — kita lihat 5 siswa lama yang paling mirip,
> kebanyakan mereka lulus atau tidak? Itu jadi tebakan kita."

**Kenapa ini gampang dijelasin:**
- Output cuma 2: **LULUS** atau **TIDAK** (bukan angka rumit).
- Algoritmanya 1 kalimat: *"lihat tetangga terdekat, ikuti mayoritas"*.
- Relate banget sama kehidupan siswa/mahasiswa.
- Grafik warna-warni, enak dilihat.

---

## 💡 Konsep Machine Learning (Singkat)

| Istilah | Artinya |
|---|---|
| **Machine Learning** | Komputer belajar dari data, bukan dari aturan manual |
| **Supervised Learning** | Belajar dari data yang sudah ada jawabannya (label) |
| **Fitur (X)** | Data input → jam belajar & jam tidur |
| **Label (y)** | Yang diprediksi → lulus atau tidak |
| **Training** | Proses model "belajar" dari data |
| **Model** | Hasil training, siap dipakai untuk prediksi |
| **KNN** | K-Nearest Neighbors: "lihat K tetangga terdekat, ikuti mayoritas" |

---

## 📁 Isi Project

```
ml trial/
├── README.md                       ← File ini (panduan)
├── requirements.txt                ← Daftar library yang dibutuhkan
│
├── prediksi_kelulusan.py           ← ⭐ PROJECT UTAMA (gampang presentasi)
├── grafik_kelulusan_1_data.png     ← Grafik data siswa (dibuat otomatis)
├── grafik_kelulusan_2_prediksi.png ← Grafik prediksi siswa baru (dibuat otomatis)
│
└── prediksi_harga_rumah.py         ← 📈 LEVEL 2: project tambahan (Linear Regression)
    grafik_1_data_asli.png          ← (dibuat saat program rumah jalan)
    grafik_2_garis_model.png       ← (dibuat saat program rumah jalan)
```

---

## 🛠️ Cara Setup & Jalankan

### 1. Install Python
Download dari: https://www.python.org/downloads/
Atau pakai Anaconda (lebih lengkap): https://www.anaconda.com/download

> Pas install Python, **centang "Add Python to PATH"** supaya bisa dipakai di terminal.

### 2. Buka Terminal di folder ini
Klik kanan di folder → "Open in Terminal" / "Open PowerShell here"

### 3. Install library (sekali aja)
```powershell
pip install -r requirements.txt
```

### 4. Jalankan project utama
```powershell
python prediksi_kelulusan.py
```

---

## 📊 Output yang Diharapkan

```
DATA SISWA LAMA (10 baris pertama)
...tabel siswa...

PEMBAGIAN DATA
Training: 16 siswa | Test: 4 siswa

UJIAN MODEL
Akurasi: 100.0%  (4 benar dari 4 siswa)

PREDIKSI SISWA BARU
Siswa baru: belajar 3 jam, tidur 6 jam
5 tetangga terdekatnya: ...tabel...
Mayoritas tetangga: LULUS
=> Prediksi model  : LULUS ✅
```

Dua file gambar `.png` otomatis terbentuk — bisa langsung dipakai buat slide.

---

## 🗣️ Script Presentasi Singkat (3 menit)

1. **Masalahnya** — Kita mau prediksi siswa baru bakal lulus atau tidak, tanpa harus nunggu ujian.
2. **Datanya** — 20 siswa lama, tiap siswa dicatat jam belajar + jam tidur + hasil ujiannya. (Tunjukkan grafik 1.)
3. **Idenya** — Kalau siswa baru kebiasaannya mirip sama siswa-siswa lama yang lulus, kemungkinan besar dia juga lulus. Itu inti algoritma **KNN**.
4. **Hasilnya** — Model uji coba akurasi tinggi. Datang siswa baru (belajar 3 jam, tidur 6 jam), kita lihat 5 siswa lama yang paling mirip, mayoritas lulus → prediksi: **LULUS**. (Tunjukkan grafik 2.)
5. **Kenapa ini Machine Learning?** — Komputer menemukan pola dari data sendiri, kita ga nulis aturan manual kayak "kalau belajar > 5 jam pasti lulus".

---

## 🚀 Level Berikutnya

Project utama pakai **klasifikasi** (output: kategori). Kalau sudah paham,
coba project kedua yang ada di folder ini:

```powershell
python prediksi_harga_rumah.py
```

Project itu pakai **Linear Regression** — prediksi **angka** (harga rumah),
bukan kategori. Konsepnya mirip tapi outputnya beda.

Tantangan lain setelah itu:
1. Tambah fitur baru (jumlah kamar, lokasi) → namanya *Multiple Regression*.
2. Coba algoritma lain: *Decision Tree*, *Random Forest*.
3. Pakai dataset nyata dari [Kaggle](https://www.kaggle.com/datasets).

---

## 📚 Sumber Belajar Gratis

- [Dicoding: Machine Learning untuk Pemula](https://www.dicoding.com/academies/184) (Bahasa Indonesia!)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Kaggle Learn](https://www.kaggle.com/learn) (gratis, interaktif)
