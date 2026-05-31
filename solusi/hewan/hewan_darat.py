# hewan_darat.py
# Middle class untuk hewan darat
# Bagian dari solusi LSP + SRP

from hewan.hewan import Hewan

class Unggas(Hewan):
    """Hewan jenis unggas - inherit Hewan"""
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

class Mamalia(Hewan):
    """Hewan jenis mamalia - inherit Hewan"""
    def makan(self):
        print(f"{self.nama} sedang makan daging/rumput.")