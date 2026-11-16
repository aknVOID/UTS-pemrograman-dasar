"""Modul untuk membaca dan menyimpan data inventaris."""

import csv
import json
from pathlib import Path


def load_items(csv_path):
    """Membaca data barang dari CSV dan mengembalikan list berisi dictionary."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"File data tidak ditemukan: {path}")

    items = []
    required = {"id", "nama", "kategori", "stok", "harga"}

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError("Format CSV tidak valid. Kolom wajib: id,nama,kategori,stok,harga")

        for line_number, row in enumerate(reader, start=2):
            try:
                item = {
                    "id": row["id"].strip(),
                    "nama": row["nama"].strip(),
                    "kategori": row["kategori"].strip(),
                    "stok": int(row["stok"]),
                    "harga": float(row["harga"]),
                }
            except (TypeError, ValueError):
                raise ValueError(f"Data tidak valid pada baris {line_number}. Periksa stok dan harga.")

            if not item["id"] or not item["nama"] or not item["kategori"]:
                raise ValueError(f"Ada kolom kosong pada baris {line_number}.")
            if item["stok"] < 0 or item["harga"] < 0:
                raise ValueError(f"Stok/harga tidak boleh negatif pada baris {line_number}.")
            items.append(item)

    ids = [item["id"] for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("Ditemukan ID barang duplikat di file CSV.")
    return items


def save_items(items, csv_path):
    """Menyimpan list barang ke file CSV."""
    path = Path(csv_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = ["id", "nama", "kategori", "stok", "harga"]
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(items)


def save_json(data, json_path):
    """Menyimpan hasil analisis ke file JSON."""
    path = Path(json_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
