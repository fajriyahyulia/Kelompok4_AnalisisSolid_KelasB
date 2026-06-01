# kebun_binatang.py
# Class KebunBinatang - solusi OCP + DIP
# Dikerjakan oleh: Wijang pratama (OCP) & Abid (DIP)

from kandang.kandang import KandangBase
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

class Perawatan:
    """Class khusus merawat hewan (SRP)
       Tidak perlu diubah jika ada hewan baru (OCP)"""
    def __init__(self, kandang: KandangBase):  # DIP - inject lewat parameter
        self.kandang = kandang

    def rawat_semua_hewan(self):
        print("\n--- Merawat Semua Hewan ---")
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):   # OCP - tidak paksa terbang()
                hewan.terbang()
            if isinstance(hewan, BisaBerenang):  # OCP - tidak paksa berenang()
                hewan.berenang()
            if isinstance(hewan, BisaBerlari):   # OCP - tidak paksa berlari()
                hewan.berlari()


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