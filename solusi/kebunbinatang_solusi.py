# kebunbinatang_solusi.py
# Analisis: OCP + DIP pada class KebunBinatang
# Dikerjakan oleh: Wijang (OCP) & Abid (DIP)

from abstraksi import KandangBase, BisaTerbang, BisaBerenang

# SOLUSI OCP + DIP
class KebunBinatang:
    def __init__(self, kandang: KandangBase):  # DIP - inject lewat parameter
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):  # OCP - tidak paksa terbang()
                hewan.terbang()
            if isinstance(hewan, BisaBerenang): # OCP - tidak paksa berenang()
                hewan.berenang()