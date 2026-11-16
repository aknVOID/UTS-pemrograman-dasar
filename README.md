# Inventory Management CLI

Aplikasi pengolahan data inventaris berbasis Command Line menggunakan Python dan standard library.

## 1. Deskripsi
Aplikasi membantu petugas gudang/toko mengelola data barang, mencari barang, memfilter kategori, menghitung stok dan nilai inventaris, serta membuat laporan CSV dan JSON.

## 2. Kebutuhan
- Python 3.9 atau lebih baru
- Tidak memerlukan library eksternal (hanya standard library)

## 3. Struktur folder
```text
inventory_management_cli/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   └── barang.csv
├── inventory/
│   ├── __init__.py
│   ├── data_manager.py
│   ├── operations.py
│   └── reports.py
└── output/
    ├── laporan_barang.csv
    └── laporan_inventaris.json
```

## 4. Cara menjalankan
1. Ekstrak ZIP.
2. Buka terminal pada folder `inventory_management_cli`.
3. Jalankan:
   ```bash
   python main.py
   ```
4. Pilih menu sesuai kebutuhan.
5. Pilih menu 7 untuk membuat laporan di folder `output/`.

## 5. Format data input CSV
Header wajib: `id,nama,kategori,stok,harga`.

Contoh:
```csv
id,nama,kategori,stok,harga
BRG001,Laptop,Elektronik,5,7500000
```
Stok harus bilangan bulat nol atau positif. Harga harus angka nol atau positif. ID harus unik.

## 6. Fitur aplikasi
- Menampilkan seluruh barang.
- Menambahkan barang dengan validasi.
- Mencari berdasarkan ID/nama.
- Memfilter berdasarkan kategori.
- Menghitung jumlah barang, total stok, dan nilai inventaris.
- Menghapus barang berdasarkan ID.
- Menampilkan kategori unik.
- Mengekspor laporan CSV dan JSON.

## 7. Penerapan konsep Python
- **List:** menyimpan kumpulan data barang.
- **Dictionary:** menyimpan atribut setiap barang dan ringkasan laporan.
- **Set:** memperoleh kategori unik dan memeriksa duplikasi ID.
- **Percabangan:** menentukan tindakan berdasarkan pilihan menu.
- **Perulangan:** menjalankan menu dan membaca setiap data.
- **Comprehension:** pencarian, filtering, dan daftar barang stok menipis.
- **Function:** setiap fungsi memiliki tanggung jawab tertentu dan nilai kembali yang jelas.
- **Package:** folder `inventory` menjadi package buatan sendiri.
- **Module:** `data_manager`, `operations`, dan `reports` memisahkan tanggung jawab program.

## 8. Alur dependensi
`main.py` memanggil fungsi pada `inventory.data_manager`, `inventory.operations`, dan `inventory.reports`.
`inventory.reports` menggunakan fungsi analisis dari `inventory.operations`.
`data_manager.py` menangani pembacaan/penyimpanan file, sedangkan `operations.py` menangani manipulasi data.

## 9. Exception handling dan defensive programming
- `FileNotFoundError`: file CSV tidak ditemukan.
- `ValueError`: angka tidak valid, kolom tidak sesuai, ID duplikat, atau data negatif.
- `OSError`: kegagalan akses file.
- Input menu dan angka divalidasi sebelum diproses.
- Kolom wajib, nilai stok/harga, dan keunikan ID diperiksa saat membaca data.

## 10. Skenario pengujian
| No. | Skenario | Hasil yang diharapkan |
|---|---|---|
| 1 | Menampilkan data awal | 7 barang tampil |
| 2 | Mencari kata Laptop | BRG001 ditemukan |
| 3 | Filter kategori Elektronik | 3 barang tampil |
| 4 | Menambah barang dengan ID baru | Data tersimpan |
| 5 | Menambah ID yang sudah ada | Ditolak dengan pesan kesalahan |
| 6 | Memasukkan stok berupa teks | Diminta memasukkan angka kembali |
| 7 | Memasukkan stok negatif | Ditolak |
| 8 | Mencari ID yang tidak ada | Pesan data tidak ditemukan/tidak ada hasil |
| 9 | Mengekspor laporan | File CSV dan JSON terbentuk |
| 10 | File CSV tidak ditemukan | Program membuat data kosong |

## 11. Debugging contoh
**Skenario error:** pengguna memasukkan `abc` pada kolom stok.
**Penyebab:** fungsi `int()` tidak dapat mengubah teks `abc` menjadi bilangan bulat.
**Perbaikan:** konversi ditempatkan di dalam `try-except ValueError`. Program menampilkan pesan bahwa input harus bilangan bulat, kemudian meminta input ulang tanpa berhenti mendadak.

## 12. Referensi
- Dokumentasi Python: https://docs.python.org/3/
- Dokumentasi modul csv: https://docs.python.org/3/library/csv.html
- Dokumentasi modul json: https://docs.python.org/3/library/json.html
- Dokumentasi pathlib: https://docs.python.org/3/library/pathlib.html

## 13. Bantuan AI
Bantuan AI digunakan untuk membantu menyusun rancangan, contoh implementasi, dokumentasi, dan pemeriksaan struktur program. Seluruh kode perlu dipahami, diuji, dan disesuaikan oleh mahasiswa sebelum dikumpulkan.
