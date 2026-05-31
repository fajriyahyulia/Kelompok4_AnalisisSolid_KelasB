# kebun_binatang.py
# Class KebunBinatang - solusi OCP + DIP
# Dikerjakan oleh: Wijang (OCP) & Abid (DIP)

from kandang.kandang import KandangBase
from layanan.perawatan import Perawatan
from layanan.pemberian_makan import PemberianMakan

class KebunBinatang:
    """KebunBinatang bergantung ke abstraksi (DIP)
       Tidak perlu diubah jika ada hewan baru (OCP)"""
    def __init__(self, kandang: KandangBase):  # DIP - inject lewat parameter
        self.kandang = kandang
        self.perawatan = Perawatan(kandang)
        self.pemberian_makan = PemberianMakan(kandang)

    def operasional_harian(self):
        print("\n=== Operasional Harian Kebun Binatang ===")
        self.pemberian_makan.beri_makan_semua()
        self.perawatan.rawat_semua_hewan()

    def bersihkan(self):
        print("\n--- Kebersihan Kandang ---")
        self.kandang.bersihkan_kandang()