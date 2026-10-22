# Pertemuan 10 — String dan Pengolahan Teks Python

## Identitas Mahasiswa
- **Nama:** Farid Syahputra
- **NIM:** 2225250222
- **Kelas:** 3F
- **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan
Mempelajari penggunaan string dalam Python, meliputi indeks, slicing, method string, pembersihan teks, pemisahan dan penggabungan kata, pencarian kata, serta penerapan fungsi untuk normalisasi data mahasiswa.

## Struktur Folder
```text
pertemuan-10-string-2225250222/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
└── tugas/
    └── normalisasi_data_mahasiswa.py
```

## Daftar Latihan
1. Dasar string: menampilkan teks, menghitung panjang, dan mengubah kapitalisasi.
2. Indeks dan slicing: mengambil karakter serta bagian teks.
3. Method string: membersihkan spasi dan mengubah kapitalisasi.
4. Membersihkan teks: merapikan spasi berlebih.
5. Split dan join: memisahkan serta menggabungkan kata.
6. Pencarian kata: menggunakan `in`, `count()`, dan `find()`.

## Algoritma Tugas 4
1. Menerima input nama mahasiswa dan kode kelas.
2. Membersihkan spasi berlebih pada nama.
3. Mengubah nama menjadi format Title Case.
4. Memisahkan nama menjadi beberapa kata.
5. Membuat inisial dari huruf pertama setiap kata.
6. Mengubah kode kelas menjadi huruf kapital.
7. Mengganti spasi pada kode kelas dengan tanda hubung.
8. Menghitung jumlah kata pada nama.
9. Menampilkan hasil normalisasi.

## Cara Menjalankan
Pastikan terminal berada di folder utama proyek.

Menjalankan latihan:
```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

Menjalankan tugas utama:
```bash
python tugas/normalisasi_data_mahasiswa.py
```

## Test Case Tugas 4

| No. | Input Nama | Input Kode | Nama Bersih | Kode Bersih | Jumlah Kata | Inisial |
|---|---|---|---|---|---:|---|
| 1 | `aan hendrayana` | `pmat a 2026` | Aan Hendrayana | PMAT-A-2026 | 2 | AH |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah | KELAS-B | 2 | FM |
| 3 | `BUDI` | `pmtk 01` | Budi | PMTK-01 | 1 | B |
| 4 | `siti nur aisyah` | `kelas c` | Siti Nur Aisyah | KELAS-C | 3 | SNA |

**Catatan:** Isi hasil aktual dan status berdasarkan hasil pengujian langsung di komputer.

## Refleksi
Pada tugas ini, saya mempelajari bahwa data teks dapat memiliki spasi dan kapitalisasi yang tidak konsisten. Masalah tersebut dapat diatasi menggunakan `strip()`, `split()`, `join()`, dan `title()`. Penggunaan fungsi membantu agar proses normalisasi dapat digunakan kembali dan kode menjadi lebih terstruktur.

## Sumber dan Bantuan
- Bahan Ajar Pertemuan 10: String dan Pengolahan Teks dalam Python.
- Dokumentasi resmi Python mengenai tipe data string.
- Bantuan AI digunakan untuk membantu memahami konsep dan menyusun kode; kode diuji kembali sebelum dikumpulkan.
