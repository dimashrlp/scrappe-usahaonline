"""Central configuration for the BPS Prabumulih scraping project.

This module keeps project constants in one place so Sprint 2 implementation can
reuse the same paths, browser options, scraping limits, dataset columns, and
logging settings consistently.
"""

from __future__ import annotations

import logging
from pathlib import Path

PROJECT_NAME = "scraping_bps_prabumulih"
PROJECT_VERSION = "1.5.0"

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DOCUMENTATION_DIR = BASE_DIR / "dokumentasi"
REPORT_DIR = BASE_DIR / "laporan"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "scraping.log"

# Browser automation defaults for the future Playwright implementation.
HEADLESS = True
TIMEOUT = 60_000
SEARCH_DELAY = 2.0
SCROLL_COUNT = 5
MAX_RESULT_PER_KEYWORD = 20
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

# Logging configuration uses Python's built-in logging module.
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

DEFAULT_LOCATION = "Kota Prabumulih, Sumatera Selatan"

FIELD_NAMES: list[str] = [
    "nama_usaha",
    "kategori",
    "alamat",
    "nomor_telepon",
    "website",
    "rating",
    "jumlah_review",
    "google_maps_url",
    "instagram",
    "facebook",
    "tiktok",
    "shopee",
    "tokopedia",
    "digital_channel",
    "keyword_pencarian",
    "waktu_scraping",
]

DEFAULT_KEYWORDS: list[str] = [
    # Kategori Kuliner
    "Coffee Shop Prabumulih",
    "Cafe Prabumulih",
    "Restoran Prabumulih",
    "Rumah Makan Prabumulih",
    "Warung Makan Prabumulih",
    "Bakso Prabumulih",
    "Mie Ayam Prabumulih",
    "Ayam Geprek Prabumulih",
    "Seafood Prabumulih",
    "Bakery Prabumulih",
    "Toko Kue Prabumulih",
    "Minuman Kekinian Prabumulih",
    # Kategori Jajanan
    "Jajanan Prabumulih",
    "Snack Prabumulih",
    "Frozen Food Prabumulih",
    "Dessert Prabumulih",
    "Catering Prabumulih",
    "Oleh-Oleh Prabumulih",
    "Seblak Prabumulih",
    "Martabak Prabumulih",
    # Kategori Fashion
    "Toko Hijab Prabumulih",
    "Toko Baju Prabumulih",
    "Toko Sepatu Prabumulih",
    "Toko Kosmetik Prabumulih",
    "Salon Prabumulih",
    "Barbershop Prabumulih",
    "Nail Art Prabumulih",
    "Skincare Prabumulih",
    # Kategori Gift
    "Florist Prabumulih",
    "Bouquet Prabumulih",
    "Hampers Prabumulih",
    "Souvenir Prabumulih",
    "Gift Shop Prabumulih",
    "Toko Kado Prabumulih",
    "Percetakan Prabumulih",
    "Merchandise Prabumulih",
    # Kategori Retail
    "Toko Mainan Prabumulih",
    "Toko Buku Prabumulih",
    "Toko ATK Prabumulih",
    "Toko Elektronik Prabumulih",
    "Toko HP Prabumulih",
    "Konter HP Prabumulih",
    "Aksesoris HP Prabumulih",
    "Toko Komputer Prabumulih",
    "Pet Shop Prabumulih",
    "Toko Perlengkapan Bayi Prabumulih",
    # Kategori Lifestyle
    "Gym Prabumulih",
    "Laundry Prabumulih",
    "Fotokopi Prabumulih",
    "Studio Foto Prabumulih",
    "Event Organizer Prabumulih",
    "Wedding Organizer Prabumulih",
    "Les Privat Prabumulih",
    "Travel Prabumulih",
    # Kategori Kesehatan
    "Apotek Prabumulih",
    "Klinik Prabumulih",
    "Optik Prabumulih",
    "Dental Clinic Prabumulih",
    "Toko Alat Kesehatan Prabumulih",
    "Laboratorium Prabumulih",
]
