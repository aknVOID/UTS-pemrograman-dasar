"""Program utama Inventory Management CLI."""

from pathlib import Path

from inventory.data_manager import load_items, save_items, save_json
from inventory.operations import (
    display_items, search_item, filter_by_category, get_categories,
    calculate_summary, add_item, delete_item
)
from inventory.reports import build_report

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "barang.csv"
OUTPUT_DIR = BASE_DIR / "output"


def read_non_empty(prompt):
    """Meminta input teks yang tidak boleh kosong."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")


def read_non_negative_int(prompt):
    """Meminta input bilangan bulat nol atau positif."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Nilai tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Input harus berupa bilangan bulat.")


def read_non_negative_float(prompt):
    """Meminta input angka nol atau positif."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Nilai tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Input harus berupa angka, contoh: 15000 atau 15000.50.")


def show_summary(items):
    """Menampilkan ringkasan inventaris."""
    summary = calculate_summary(items)
    print("\n=== RINGKASAN INVENTARIS ===")
    print(f"Jumlah jenis barang : {summary['jumlah_jenis_barang']}")
    print(f"Jumlah kategori     : {summary['jumlah_kategori']}")
    print(f"Total stok          : {summary['total_stok']}")
    print(f"Nilai inventaris    : Rp{summary['total_nilai_inventaris']:,.2f}")
    print("Barang dengan stok <= 5:")
    if summary["barang_stok_menipis"]:
        for item in summary["barang_stok_menipis"]:
            print(f"- {item['nama']} (ID: {item['id']}), stok: {item['stok']}")
    else:
        print("- Tidak ada")


def main():
    """Menjalankan menu utama aplikasi."""
    try:
        items = load_items(DATA_FILE)
    except FileNotFoundError:
        print("File data belum tersedia. Membuat file data kosong.")
        items = []
        save_items(items, DATA_FILE)
    except (ValueError, OSError) as error:
        print(f"Gagal membaca data: {error}")
        return

    while True:
        print("\n" + "=" * 42)
        print("       INVENTORY MANAGEMENT CLI")
        print("=" * 42)
        print("1. Tampilkan semua barang")
        print("2. Tambah barang")
        print("3. Cari barang")
        print("4. Filter berdasarkan kategori")
        print("5. Tampilkan ringkasan inventaris")
        print("6. Hapus barang")
        print("7. Ekspor laporan CSV dan JSON")
        print("8. Tampilkan kategori unik")
        print("0. Keluar")

        choice = input("Pilih menu: ").strip()

        try:
            if choice == "1":
                print("\n" + display_items(items))

            elif choice == "2":
                new_item = {
                    "id": read_non_empty("ID barang: "),
                    "nama": read_non_empty("Nama barang: "),
                    "kategori": read_non_empty("Kategori: "),
                    "stok": read_non_negative_int("Stok: "),
                    "harga": read_non_negative_float("Harga satuan: "),
                }
                add_item(items, new_item)
                save_items(items, DATA_FILE)
                print("Barang berhasil ditambahkan.")

            elif choice == "3":
                keyword = read_non_empty("Masukkan ID atau nama barang: ")
                results = search_item(items, keyword)
                print(display_items(results))

            elif choice == "4":
                print("Kategori tersedia:", ", ".join(sorted(get_categories(items))) or "(kosong)")
                category = read_non_empty("Masukkan kategori: ")
                results = filter_by_category(items, category)
                print(display_items(results))

            elif choice == "5":
                show_summary(items)

            elif choice == "6":
                item_id = read_non_empty("Masukkan ID barang yang dihapus: ")
                items, deleted = delete_item(items, item_id)
                if deleted:
                    save_items(items, DATA_FILE)
                    print("Barang berhasil dihapus.")
                else:
                    print("ID tidak ditemukan.")

            elif choice == "7":
                save_items(items, OUTPUT_DIR / "laporan_barang.csv")
                report = build_report(items)
                save_json(report, OUTPUT_DIR / "laporan_inventaris.json")
                print("Laporan berhasil disimpan di folder output/.")

            elif choice == "8":
                categories = sorted(get_categories(items))
                print("Kategori unik:", ", ".join(categories) if categories else "Belum ada kategori.")

            elif choice == "0":
                print("Terima kasih. Program selesai.")
                break

            else:
                print("Pilihan menu tidak tersedia. Masukkan angka 0 sampai 8.")

        except ValueError as error:
            print(f"Data tidak dapat diproses: {error}")
        except OSError as error:
            print(f"Terjadi kesalahan saat mengakses file: {error}")


if __name__ == "__main__":
    main()
