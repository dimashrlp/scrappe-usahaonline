# scraping_bps_prabumulih

`scraping_bps_prabumulih` adalah project Python untuk tugas seleksi magang BPS Kota Prabumulih posisi Asisten Pranata Komputer. Project ini disiapkan untuk melakukan scraping data usaha online yang berlokasi di Kota Prabumulih dengan Google Maps sebagai sumber utama dan Google Search sebagai tahap verifikasi kanal digital.

> Status saat ini: Sprint 2.1. Project sudah dapat menjalankan validasi awal Playwright untuk membuka Google Maps, mengetik keyword pertama, menunggu hasil pencarian, dan menutup browser. Project belum melakukan scraping data.

## Tujuan Project

Project ini dirancang agar reviewer dapat memahami rancangan teknis sebelum proses scraping dimulai. Fondasi ini menekankan:

1. Struktur folder yang rapi dan stabil.
2. Data model final berbasis dataclass.
3. Konfigurasi terpusat untuk browser automation, output, logging, dan keyword.
4. Pipeline data yang jelas dari keyword sampai output CSV/Excel.
5. Pemisahan tanggung jawab antara scraping, verifikasi, cleaning, export, dokumentasi, laporan, dan log.

## Teknologi yang Digunakan

- Python 3.11+
- Playwright untuk browser automation pada Sprint 2
- Pandas untuk pengolahan data tabular
- OpenPyXL untuk ekspor Excel melalui Pandas
- Logging bawaan Python untuk pencatatan proses ke console dan `logs/scraping.log`

## Arsitektur Project

Project menggunakan arsitektur modular sederhana agar mudah dikembangkan tanpa mengubah struktur folder pada sprint berikutnya.

```text
scraping_bps_prabumulih/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── scraper/
│   ├── __init__.py
│   ├── maps_scraper.py
│   ├── google_maps_page.py
│   └── search_verifier.py
├── processing/
│   ├── __init__.py
│   ├── cleaning.py
│   └── exporter.py
├── output/
├── dokumentasi/
├── laporan/
└── logs/
```

## Penjelasan Setiap Folder dan File

- `main.py`: entry point project dan utilitas awal konfigurasi logging.
- `config.py`: konfigurasi project, versi, folder, parameter scraping, logging, nama kolom dataset, lokasi default, dan daftar keyword.
- `requirements.txt`: daftar dependensi minimal untuk menjalankan project.
- `scraper/`: package untuk modul scraping dan verifikasi sumber data.
- `scraper/maps_scraper.py`: data model final `BusinessRecord` dan coordinator `MapsScraper` untuk alur Sprint 2.1.
- `scraper/google_maps_page.py`: Page Object Model untuk membuka Google Maps, mengetik keyword, menunggu hasil pencarian, dan menutup browser.
- `scraper/search_verifier.py`: template class untuk verifikasi relevansi lokasi dan duplikasi data.
- `processing/`: package untuk cleaning dan export data.
- `processing/cleaning.py`: placeholder fungsi cleaning seperti normalisasi nomor telepon, rating, jumlah review, alamat, duplikasi, dan kanal digital.
- `processing/exporter.py`: helper ekspor CSV/Excel dengan urutan kolom final.
- `output/`: folder hasil scraping dalam format CSV dan Excel.
- `dokumentasi/`: folder tangkapan layar proses scraping dan bukti langkah kerja.
- `laporan/`: folder laporan akhir untuk reviewer.
- `logs/`: folder file log proses, termasuk `scraping.log`.

## Data Pipeline

Project akan dikembangkan dengan alur kerja berikut.

```text
Keyword
   │
   ▼
Google Maps
   │
   ▼
Raw Data
   │
   ▼
Google Search Verification
   │
   ▼
Cleaning
   │
   ▼
Data Analysis
   │
   ▼
CSV + Excel
```

### Penjelasan Pipeline

1. **Keyword**: daftar keyword disiapkan berdasarkan kategori usaha yang relevan untuk Kota Prabumulih.
2. **Google Maps**: Sprint 2 akan mengambil data usaha dari hasil pencarian Google Maps.
3. **Raw Data**: data awal akan disimpan dalam bentuk record sesuai model final.
4. **Google Search Verification**: kanal digital seperti Instagram, Facebook, TikTok, Shopee, dan Tokopedia akan diverifikasi dari pencarian Google Search.
5. **Cleaning**: data akan dibersihkan agar nomor telepon, rating, jumlah review, alamat, dan kanal digital lebih konsisten.
6. **Data Analysis**: data siap diringkas untuk kebutuhan laporan BPS.
7. **CSV + Excel**: output akhir disimpan ke folder `output/`.

## Dataset Final

Setiap baris dataset merepresentasikan satu usaha di Kota Prabumulih. Kolom final yang disiapkan adalah:

| No | Kolom | Keterangan |
|---:|---|---|
| 1 | `nama_usaha` | Nama usaha dari Google Maps. |
| 2 | `kategori` | Kategori usaha. |
| 3 | `alamat` | Alamat usaha. |
| 4 | `nomor_telepon` | Nomor telepon jika tersedia. |
| 5 | `website` | Website resmi jika tersedia. |
| 6 | `rating` | Rating Google Maps. |
| 7 | `jumlah_review` | Jumlah ulasan Google Maps. |
| 8 | `google_maps_url` | URL detail usaha di Google Maps. |
| 9 | `instagram` | Link Instagram terverifikasi jika ditemukan. |
| 10 | `facebook` | Link Facebook terverifikasi jika ditemukan. |
| 11 | `tiktok` | Link TikTok terverifikasi jika ditemukan. |
| 12 | `shopee` | Link Shopee terverifikasi jika ditemukan. |
| 13 | `tokopedia` | Link Tokopedia terverifikasi jika ditemukan. |
| 14 | `digital_channel` | Ringkasan kanal digital yang tersedia. |
| 15 | `keyword_pencarian` | Keyword yang menghasilkan data usaha. |
| 16 | `waktu_scraping` | Waktu pengambilan data. |

## Keyword Pencarian

Keyword disusun untuk mencakup berbagai jenis usaha yang umum ditemukan secara online di Kota Prabumulih. Daftar lengkap disimpan di `DEFAULT_KEYWORDS` pada `config.py` dan dikelompokkan berdasarkan kategori berikut:

- Kuliner: coffee shop, cafe, restoran, rumah makan, bakso, mie ayam, ayam geprek, seafood, bakery, toko kue, dan minuman kekinian.
- Jajanan: jajanan, snack, frozen food, dessert, catering, oleh-oleh, seblak, dan martabak.
- Fashion: hijab, baju, sepatu, kosmetik, salon, barbershop, nail art, dan skincare.
- Gift: florist, bouquet, hampers, souvenir, gift shop, toko kado, percetakan, dan merchandise.
- Retail: mainan, buku, ATK, elektronik, HP, konter HP, aksesoris HP, komputer, pet shop, dan perlengkapan bayi.
- Lifestyle: gym, laundry, fotokopi, studio foto, event organizer, wedding organizer, les privat, dan travel.
- Kesehatan: apotek, klinik, optik, dental clinic, alat kesehatan, dan laboratorium.

## Logging

Logging disiapkan menggunakan modul bawaan Python. Ketika `python main.py` dijalankan, log akan tampil di console dan disimpan ke:

```text
logs/scraping.log
```

Format log dibuat konsisten agar proses scraping di Sprint 2 mudah diaudit dan ditelusuri.

## Instalasi

1. Buat virtual environment.

   ```bash
   python -m venv .venv
   ```

2. Aktifkan virtual environment.

   ```bash
   source .venv/bin/activate
   ```

3. Instal dependensi Python.

   ```bash
   pip install -r requirements.txt
   ```

4. Instal browser Playwright saat masuk Sprint 2.

   ```bash
   playwright install
   ```

## Cara Menjalankan Template

```bash
python main.py
```

Perintah tersebut menjalankan validasi Sprint 2.1: membuka Chromium dengan Playwright, membuka Google Maps, mengetik keyword pertama dari `DEFAULT_KEYWORDS`, menunggu hasil pencarian, lalu menutup browser. Perintah ini belum melakukan scraping, scrolling, parsing, atau export.

## Roadmap Project

- **Sprint 1 ✅**: membuat struktur folder, file dasar, dan dokumentasi awal.
- **Sprint 1.5 ✅**: memperkuat data model, konfigurasi, keyword, cleaning placeholder, exporter, logging, dan README.
- **Sprint 2.1 ✅**: validasi Playwright, Chromium, Google Maps, input keyword, hasil pencarian, dan penutupan browser.
- **Sprint 2**: implementasi scraping Google Maps menggunakan Playwright.
- **Sprint 3**: implementasi cleaning lanjutan, deduplikasi, validasi lokasi, dan verifikasi Google Search.
- **Sprint 4**: analisis data, finalisasi output CSV/Excel, dokumentasi proses, dan laporan akhir.

## Batasan Saat Ini

- Belum ada fitur scraping.
- Belum ada parser HTML.
- Belum ada proses Google Search.
- Belum ada data output final.

Batasan ini disengaja agar fondasi project matang sebelum implementasi scraping dimulai.
