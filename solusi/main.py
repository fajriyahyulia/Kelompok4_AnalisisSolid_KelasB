# main.py - File integrasi semua solusi SOLID
# Dibuat oleh: Fajriyah

from hewan_solusi import Burung, Ikan, Kucing
from kandang_solusi import Kandang, PetugasKebersihan
from kebunbinatang_solusi import KebunBinatang

if __name__ == "__main__":
    print("=== Kelompok 4 - Solusi Prinsip SOLID ===\n")

    # Buat hewan
    burung = Burung("Cici", "Burung")
    ikan = Ikan("Nemo", "Ikan")
    kucing = Kucing("Mimi", "Kucing")

    # Buat kandang dan tambah hewan
    kandang = Kandang()
    kandang.tambah_hewan(burung)
    kandang.tambah_hewan(ikan)
    kandang.tambah_hewan(kucing)

    # Rawat semua hewan
    print("--- Merawat Hewan ---")
    kebun = KebunBinatang(kandang)
    kebun.rawat_semua_hewan()

    # Bersihkan kandang
    print("\n--- Kebersihan Kandang ---")
    petugas = PetugasKebersihan()
    petugas.bersihkan_kandang(kandang)

    print("\nSelesai!")