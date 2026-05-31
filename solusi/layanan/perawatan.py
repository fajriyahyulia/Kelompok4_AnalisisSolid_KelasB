# perawatan.py
# Class Perawatan - solusi SRP + OCP
# Dikerjakan oleh: Wijang

from kandang.kandang import KandangBase
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

class Perawatan:
    """Class khusus untuk merawat hewan (SRP)
       Tidak perlu diubah jika ada hewan baru (OCP)"""
    def __init__(self, kandang: KandangBase):  # DIP - inject lewat parameter
        self.kandang = kandang

    def rawat_semua_hewan(self):
        print("\n--- Merawat Semua Hewan ---")
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):   # OCP - cek kemampuan terbang
                hewan.terbang()
            if isinstance(hewan, BisaBerenang):  # OCP - cek kemampuan berenang
                hewan.berenang()
            if isinstance(hewan, BisaBerlari):   # OCP - cek kemampuan berlari
                hewan.berlari()