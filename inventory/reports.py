"""Modul pembuatan laporan inventaris."""

from inventory.operations import calculate_summary, get_stock_value_by_category


def build_report(items):
    """Membentuk dictionary laporan lengkap untuk diekspor ke JSON."""
    return {
        "ringkasan": calculate_summary(items),
        "nilai_inventaris_per_kategori": get_stock_value_by_category(items),
    }
