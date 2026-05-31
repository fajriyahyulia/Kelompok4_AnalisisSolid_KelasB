# kandang_solusi.py
# Analisis: SRP + DIP pada class Kandang
# Dikerjakan oleh: Viko

from abstraksi import HewanBase, KandangBase

# SOLUSI SRP + DIP
class Kandang(KandangBase):
    """Kandang konkret, hanya bertanggung jawab menyimpan hewan"""
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan: HewanBase):
        self.hewan_list.append(hewan)

    def get_semua_hewan(self):
        return self.hewan_list

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")