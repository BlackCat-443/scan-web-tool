# Scan Web Tool & Website Traffic Monitor

Alat pemindaian web dan pemantauan lalu lintas website secara real-time.

## Deskripsi

Scan Web Tool dan Website Traffic Monitor adalah aplikasi Python yang memungkinkan pengguna untuk memantau lalu lintas website, waktu respons, dan mendeteksi potensi serangan atau anomali dalam lalu lintas web. Tool ini menampilkan grafik real-time untuk visualisasi data monitoring.

## Fitur

- Pemantauan lalu lintas web real-time
- Grafik interaktif untuk jumlah permintaan per detik dan waktu respons  
- Deteksi anomali lalu lintas
- Peringatan otomatis untuk lalu lintas mencurigakan
- Logging aktivitas
- Visualisasi data dalam bentuk grafik

## Prasyarat

Sebelum menggunakan tool ini, pastikan Anda telah menginstal:

- Python 3.6 atau lebih tinggi
- pip (Python package manager)

## Instalasi

1. Clone repositori:
```bash
git clone https://github.com/BlackCat-443/scan-web-tool.git

2. Masuk ke direktori proyek:
```bash
cd scan-web-tool

3. Instal library yang diperlukan dengan menjalankan perintah berikut di terminal:
```bash
pip install requests matplotlib

4. Instal dependensi yang diperlukan:
```bash
pip install -r requirements.txt

5. Jalankan program:
```bash
python scan_web.py

6. Masukkan URL website yang ingin dipantau

7. Program akan mulai memantau dan menampilkan:
   - Grafik real-time requests per detik
   - Grafik waktu respons
   - Peringatan untuk lalu lintas mencurigakan

8. Untuk menghentikan, tekan Ctrl+C

Konfigurasi:
Anda dapat mengubah beberapa parameter di dalam skrip:
- suspicious_threshold: Ambang batas untuk menandai lalu lintas mencurigakan (default: 50 req/s)
- Interval pemantauan dan pembaruan grafik dapat disesuaikan dalam fungsi monitor_traffic() dan FuncAnimation()

Struktur Proyek:
scan-web-tool/
│
├── scan_web.py          # Tool pemindaian web
├── website_monitor.py   # Tool monitoring traffic
├── requirements.txt     # Daftar dependensi
├── README.md           # Dokumentasi
└── .gitignore         # File konfigurasi git

Requirements.txt:
requests>=2.25.1
matplotlib>=3.3.4



Author:
- BlackCat-443

