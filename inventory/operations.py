"""Modul operasi/manipulasi data inventaris."""


def display_items(items):
    """Mengembalikan daftar barang dalam bentuk teks tabel sederhana."""
    if not items:
        return "Belum ada data barang."

    lines = [
        f"{'ID':<8} {'Nama':<22} {'Kategori':<15} {'Stok':>6} {'Harga':>14}",
        "-" * 70,
    ]
    for item in items:
        lines.append(
            f"{item['id']:<8} {item['nama']:<22} {item['kategori']:<15} "
            f"{item['stok']:>6} Rp{item['harga']:>12,.2f}"
        )
    return "\n".join(lines)


def search_item(items, keyword):
    """Mencari barang berdasarkan ID atau nama."""
    key = keyword.strip().lower()
    return [
        item for item in items
        if key in item["id"].lower() or key in item["nama"].lower()
    ]


def filter_by_category(items, category):
    """Memfilter barang berdasarkan kategori."""
    target = category.strip().lower()
    return [item for item in items if item["kategori"].lower() == target]


def get_categories(items):
    """Menghasilkan set kategori unik."""
    return {item["kategori"] for item in items}


def calculate_summary(items):
    """Menghitung jumlah jenis barang, total stok, dan nilai inventaris."""
    total_stock = sum(item["stok"] for item in items)
    total_value = sum(item["stok"] * item["harga"] for item in items)
    category_count = len({item["kategori"] for item in items})
    low_stock = [item for item in items if item["stok"] <= 5]

    return {
        "jumlah_jenis_barang": len(items),
        "jumlah_kategori": category_count,
        "total_stok": total_stock,
        "total_nilai_inventaris": round(total_value, 2),
        "barang_stok_menipis": [
            {"id": item["id"], "nama": item["nama"], "stok": item["stok"]}
            for item in low_stock
        ],
    }


def add_item(items, item):
    """Menambahkan barang jika ID belum digunakan dan data valid."""
    if any(existing["id"].lower() == item["id"].lower() for existing in items):
        raise ValueError("ID barang sudah digunakan.")
    if not item["id"].strip() or not item["nama"].strip() or not item["kategori"].strip():
        raise ValueError("ID, nama, dan kategori wajib diisi.")
    if item["stok"] < 0 or item["harga"] < 0:
        raise ValueError("Stok dan harga tidak boleh negatif.")
    items.append(item)
    return items


def delete_item(items, item_id):
    """Menghapus barang berdasarkan ID; mengembalikan list dan status."""
    filtered = [item for item in items if item["id"].lower() != item_id.strip().lower()]
    return filtered, len(filtered) != len(items)


def get_stock_value_by_category(items):
    """Mengelompokkan nilai stok berdasarkan kategori."""
    result = {}
    for item in items:
        category = item["kategori"]
        result[category] = result.get(category, 0) + item["stok"] * item["harga"]
    return result
