# kandang_solusi.py
# Analisis: SRP + DIP pada class Kandang
# Dikerjakan oleh: Viko

from abstraksi import HewanBase, KandangBase

# ============================================
# VIKO - SRP + DIP
# ============================================
# SRP: Class Kandang hanya bertanggung jawab
#      menyimpan hewan dan membersihkan kandang
# DIP: Kandang inherit KandangBase (abstraksi)
#      bukan class konkret langsung
# ============================================

class Kandang(KandangBase):
    """Kandang konkret inherit KandangBase (DIP)"""
    def __init__(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []

    def tambah_hewan(self, hewan: HewanBase):
        self.hewan_list.append(hewan)
        print(f"{hewan.nama} ditambahk