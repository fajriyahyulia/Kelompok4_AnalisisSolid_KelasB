# main.py - File integrasi semua solusi SOLID
# Dibuat oleh: Fajriyah

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hewan.hewan_terbang import Elang, Burung, Ayam, Bebek, Singa, Sapi, Ikan, Penyu
from kandang.kandang import Kandang
from kebun_binatang.kebun_binatang import KebunBinatang

if __name__ == "__main__":
    print("=== Kelompok 4 - Solusi Prinsip SOLID ===")

    # Buat kandang
    kandang = Kandang("Kandang Utama")

    # Tambah hewan
    print("\n--- Menambah Hewan ---")
    kandang.tambah_hewan(Elang("Elang Jawa", "Jawa"))
    kandang.tambah_hewan(Burung("Burung Pipit", "Indonesia"))
    kandang.tambah_hewan(Ayam("Ayam Kampung", "Indonesia"))
    kandang.tambah_hewan(Bebek("Bebek Peking", "China"))
    kandang.tambah_hewan(Singa("Singa Afrika", "Afrika"))
    kandang.tambah_hewan(Sapi("Sapi Jawa", "Jawa"))
    kandang.tambah_hewan(Ikan("Ikan Nemo", "Laut Coral"))
    kandang.tambah_hewan(Penyu("Penyu Hijau", "Samudra"))

    # Operasional harian
    kebun = KebunBinatang(kandang)
    kebun.operasional_harian()

    # Bersihkan kandang
    kebun.bersihkan()

    print("\nSelesai!")