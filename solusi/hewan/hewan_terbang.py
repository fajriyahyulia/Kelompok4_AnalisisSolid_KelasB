# hewan_terbang.py
# Analisis: SRP + ISP pada class Hewan
# Dikerjakan oleh: Fatimah

from hewan.hewan_darat import Unggas, Mamalia
from hewan.hewan import Hewan
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

# ============================================
# ANALISIS PELANGGARAN - Fatimah
# ============================================
# SRP: Class Hewan memiliki method terbang()
#      padahal tidak semua hewan bisa terbang.
#      Seharusnya tiap class punya 1 tanggung
#      jawab saja.
# ISP: Semua hewan dipaksa punya method
#      terbang() padahal tidak semua bisa.
#      Seharusnya interface dipisah sesuai
#      kemampuan masing-masing hewan.
# ============================================

# SOLUSI SRP - tiap class punya 1 tanggung jawab
# SOLUSI ISP - interface dipisah sesuai kemampuan

class Elang(Unggas, BisaTerbang):
    """Elang inherit Unggas, implement BisaTerbang (ISP)"""
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

class Ayam(Unggas, BisaBerlari):
    """Ayam inherit Unggas, implement BisaBerlari (ISP)"""
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

class Singa(Mamalia, BisaBerlari):
    """Singa inherit Mamalia, implement BisaBerlari (ISP)"""
    def berlari(self):
        print(f"{self.nama} sedang berlari kencang.")

class Ikan(Hewan, BisaBerenang):
    """Ikan inherit Hewan, implement BisaBerenang (ISP)"""
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Bebek(Unggas, BisaTerbang, BisaBerenang):
    """Bebek inherit Unggas, implement BisaTerbang+BisaBerenang (ISP)"""
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Sapi(Mamalia, BisaBerlari):
    """Sapi inherit Mamalia, implement BisaBerlari (ISP)"""
    def berlari(self):
        print(f"{self.nama} sedang berlari pelan.")

class Penyu(Hewan, BisaBerenang):
    """Penyu inherit Hewan, implement BisaBerenang (ISP)"""
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def berenang(self):
        print(f"{self.nama} sedang berenang pelan.")

class Burung(Unggas, BisaTerbang):
    """Burung inherit Unggas, implement BisaTerbang (ISP)"""
    def terbang(self):
        print(f"{self.nama} sedang terbang.")