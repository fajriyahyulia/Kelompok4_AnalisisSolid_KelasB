# kebunbinatang_solusi.py
# Analisis: OCP + DIP pada class KebunBinatang
# Dikerjakan oleh: Wijang (OCP) & Abid (DIP)

from abstraksi import KandangBase, BisaTerbang, BisaBerenang, BisaBerlari

# ============================================
# WIJANG - OCP
# ============================================
# OCP: KebunBinatang tidak perlu diubah
#      jika ada hewan baru ditambahkan.
#      Pakai isinstance check sehingga
#      terbuka untuk ekstensi tapi
#      tertutup untuk modifikasi.
# ============================================

# ============================================
# ABID - DIP
# ============================================
# DIP: KebunBinatang bergantung ke abstraksi
#      KandangBase, bukan class Kandang langsung.
#      Kandang diinject lewat parameter
#      constructor, bukan dibuat di dalam.
# ============================================

class KebunBinatang:
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