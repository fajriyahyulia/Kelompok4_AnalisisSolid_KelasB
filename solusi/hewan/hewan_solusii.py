# hewan_terbang.py
# Analisis: LSP pada class Hewan
# Dikerjakan oleh: Rahma

from hewan.hewan_darat import Unggas, Mamalia
from hewan.hewan import Hewan
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

# ============================================
# ANALISIS PELANGGARAN - Rahma
# ============================================
# LSP: Jika dibuat subclass Sapi(Hewan),
#      method terbang() tetap ada padahal
#      sapi tidak bisa terbang.
#      Memanggil sapi.terbang() menghasilkan
#      perilaku yang tidak logis dan merusak
#      program.
#      Solusi: setiap subclass hanya implement
#      kemampuan yang sesuai hewannya sehingga
#      subclass bisa menggantikan parent class
#      tanpa merusak logika program.
# ============================================

# SOLUSI LSP - setiap subclass hanya implement
# kemampuan yang sesuai dengan hewannya

class Elang(Unggas, BisaTerbang):
    """LSP: Elang bisa menggantikan Unggas tanpa error"""
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

class Ayam(Unggas, BisaBerlari):
    """LSP: Ayam bisa menggantikan Unggas tanpa error"""
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

class Bebek(Unggas, BisaTerbang, BisaBerenang):
    """LSP: Bebek bisa menggantikan Unggas tanpa error"""
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Burung(Unggas, BisaTerbang):
    """LSP: Burung bisa menggantikan Unggas tanpa error"""
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Singa(Mamalia, BisaBerlari):
    """LSP: Singa bisa menggantikan Mamalia tanpa error"""
    def berlari(self):
        print(f"{self.nama} sedang berlari kencang.")

class Sapi(Mamalia, BisaBerlari):
    """LSP: Sapi bisa menggantikan Mamalia tanpa error"""
    def berlari(self):
        print(f"{self.nama} sedang berlari pelan.")

class Ikan(Hewan, BisaBerenang):
    """LSP: Ikan bisa menggantikan Hewan tanpa error"""
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Penyu(Hewan, BisaBerenang):
    """LSP: Penyu bisa menggantikan Hewan tanpa error"""
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def berenang(self):
        print(f"{self.nama} sedang berenang pelan.")