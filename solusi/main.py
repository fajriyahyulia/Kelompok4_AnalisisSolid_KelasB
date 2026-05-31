# main.py - File integrasi semua solusi SOLID
# Dibuat oleh: Fajriya (Ketua)

from hewan_solusi import Elang, Ayam, Singa, Ikan, Bebek, Sapi, Penyu, Burung
from kandang_solusi import Kandang
from kebunbinatang_solusi import KebunBinatang

if __name__ == "__main__":
    print("=== Kelompok 4 - Solusi Prinsip SOLID ===")

    # Buat kandang
    kandang = Kandang("Kandang Utama")

    # Tambah hewan
    print("\n--- Menambah Hewan ---")
    kandang.tambah_hewan(Elang("Elang Jawa", "Jawa"))
    kandang.tambah_hewan(Ayam("Ayam Kampung", "Indonesia"))
    kandang.tambah_hewan(Singa("Singa Afrika", "Afrika"))
    kandang.tambah_hewan(Ikan("Ikan Nemo", "Laut Coral"))
    kandang.tambah_hewan(Bebek("Bebek Peking", "China"))
    kandang.tambah_hewan(Sapi("Sapi Jawa", "Jawa"))
    kandang.tambah_hewan(Penyu("Penyu Hijau", "Samudra"))
    kandang.tambah_hewan(Burung("Burung Pipit", "Indonesia"))

    # Rawat semua hewan
    kebun = KebunBinatang(kandang)
    kebun.rawat_semua_hewan()

    # Bersihkan kandang
    print("\n--- Kebersihan Kandang ---")
    kandang.bersihkan_kandang()

    print("\nSelesai!")