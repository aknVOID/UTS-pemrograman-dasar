# LEMBAR JAWABAN UTS PEMROGRAMAN DASAR
## Aplikasi Inventory Management CLI

### 1. Analisis Masalah dan Rancangan Aplikasi
Permasalahan yang dipilih adalah pengelolaan inventaris barang. Pencatatan manual dapat menyebabkan kesulitan saat mencari barang, mengetahui jumlah stok, dan menghitung nilai persediaan. Oleh karena itu, dibuat aplikasi berbasis command line menggunakan Python.

**Tujuan:** mempermudah pencatatan, pencarian, pengelompokan, dan rekapitulasi data inventaris.

**Target pengguna:** petugas gudang, pemilik toko, atau administrator inventaris.

**Input:** file CSV dengan kolom ID, nama, kategori, stok, dan harga. Pengguna juga dapat memasukkan data melalui menu CLI.

**Output:** daftar barang pada terminal serta laporan CSV dan JSON.

**Fitur utama:** menampilkan barang, menambah dan menghapus barang, mencari barang, memfilter kategori, menghitung ringkasan, serta mengekspor laporan.

### 2. Struktur Data dan Manipulasi
Program menggunakan tiga struktur data:
1. **List** untuk menyimpan seluruh barang karena data dapat ditambah, dihapus, dan diiterasi.
2. **Dictionary** untuk menyimpan atribut satu barang dalam pasangan key-value, misalnya `id`, `nama`, `kategori`, `stok`, dan `harga`.
3. **Set** untuk memperoleh kategori unik dan membantu memeriksa ID yang duplikat.

Manipulasi data diterapkan melalui pencarian ID/nama, filter kategori, pengelompokan nilai inventaris berdasarkan kategori, dan perhitungan total stok serta nilai inventaris.

### 3. Control Flow dan Pythonic Programming
- **Percabangan:** `if`, `elif`, dan `else` digunakan untuk menentukan menu yang dijalankan.
- **Perulangan:** `while` digunakan untuk mengulang menu sampai pengguna memilih keluar; `for` digunakan untuk memproses data.
- **Comprehension:** list comprehension digunakan pada pencarian, filter kategori, dan daftar barang stok menipis. Set comprehension digunakan untuk mengambil kategori unik.

**Edge case:** input stok berupa teks, stok/harga negatif, ID duplikat, file tidak ditemukan, dan pencarian tanpa hasil. Program memberikan pesan kesalahan atau hasil kosong tanpa berhenti secara tidak semestinya.

### 4. Function, Module, dan Package
Program dipecah menjadi beberapa bagian berdasarkan prinsip single responsibility.

| File | Tanggung jawab |
|---|---|
| `main.py` | Menu CLI dan alur utama |
| `inventory/data_manager.py` | Membaca dan menyimpan CSV/JSON |
| `inventory/operations.py` | Pencarian, filter, tambah, hapus, dan rekap |
| `inventory/reports.py` | Membentuk laporan |
| `inventory/__init__.py` | Menandai folder inventory sebagai package |

Contoh function:
- `load_items(csv_path)` membaca CSV dan mengembalikan list dictionary.
- `search_item(items, keyword)` mencari barang dan mengembalikan list hasil.
- `calculate_summary(items)` mengembalikan dictionary ringkasan.
- `add_item(items, item)` menambahkan data dan mengembalikan list.
- `build_report(items)` membentuk dictionary laporan.

Alur dependensi dimulai dari `main.py` yang memanggil module dalam package `inventory`. Module `reports.py` memanfaatkan fungsi analisis dari `operations.py`.

### 5. Pemrosesan File CSV/JSON
Data awal dibaca dari `data/barang.csv`. Setelah dibaca, data dikonversi menjadi list dictionary, kemudian dapat dicari, difilter, dan dihitung. Perubahan data disimpan kembali ke CSV. Hasil analisis disimpan ke `output/laporan_inventaris.json`.

Contoh input tersedia pada `data/barang.csv`. File keluaran dibuat melalui menu 7.

### 6. Exception Handling, Debugging, dan Dokumentasi
Program menangani `FileNotFoundError`, `ValueError`, dan `OSError`. Validasi dilakukan terhadap kolom CSV, data kosong, stok/harga negatif, ID duplikat, pilihan menu, dan input angka.

Contoh debugging: ketika pengguna memasukkan teks `abc` pada input stok, konversi integer menghasilkan `ValueError`. Penanganan dilakukan dengan `try-except` agar pengguna diminta memasukkan angka kembali.

Petunjuk instalasi, struktur folder, cara menjalankan, fitur, dependensi, dan skenario pengujian tersedia pada `README.md`.

### Kesimpulan
Aplikasi Inventory Management CLI menerapkan konsep dasar Python berupa struktur data, control flow, comprehension, function, module, package, pemrosesan CSV/JSON, serta exception handling. Aplikasi dapat dijalankan melalui terminal dan diuji menggunakan data contoh.
