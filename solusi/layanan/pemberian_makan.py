# pemberian_makan.py
# Class PemberianMakan - solusi SRP
# Dikerjakan oleh: Fatimah

from kandang.kandang import KandangBase

class PemberianMakan:
    """Class khusus untuk memberi makan hewan (SRP)
       Dipisah dari perawatan agar tiap class
       hanya punya 1 tanggung jawab"""
    def __init__(self, kandang: KandangBase):  # DIP - inject lewat parameter
        self.kandang = kandang

    def beri_makan_semua(self):
        print("\n--- Memberi Makan Semua Hewan ---")
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()