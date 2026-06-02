# hewan_terbang.py
# Analisis: SRP + ISP + LSP pada class Hewan
# Dikerjakan oleh: Fatimah (SRP+ISP) & Rahma (LSP)

from hewan.hewan_darat import Unggas, Mamalia
from hewan.hewan import Hewan
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

# ============================================
# ANALISIS PELANGGARAN - Fatimah (SRP + ISP)
# ============================================
# SRP: Class Hewan memiliki method terbang()
#      padahal tidak semua hewan bisa terbang.
#      Class menanggung perilaku yang tidak
#      relevan untuk semua objeknya.
# ISP: Semua hewan dipaksa punya method
#      terbang() padahal tidak semua bisa.
#      Seharusnya interface dipisah sesuai
#      kemampuan masing-masing hewan.
# ============================================

# ============================================
# ANALISIS PELANGGARAN - Rahma (LSP)
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

# Unggas yang bisa terbang
class Elang(Unggas, BisaTerbang):
    """LSP: Elang bisa menggantikan Unggas tanpa error"""
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

class Burung(Unggas, BisaTerbang):
    """LSP: Burung bisa menggantikan Unggas tanpa error"""
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Ayam(Unggas, BisaBerlari):
    """ISP: Ayam tidak dipaksa terbang, hanya berlari"""
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

# Unggas yang bisa terbang dan berenang
class Bebek(Unggas, BisaTerbang, BisaBerenang):
    """ISP: Bebek implement BisaTerbang+BisaBerenang sesuai kemampuan"""
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

# Mamalia
class Singa(Mamalia, BisaBerlari):
    """LSP: Singa bisa menggantikan Mamalia tanpa error"""
    def berlari(self):
        print(f"{self.nama} sedang berlari kencang.")

class Sapi(Mamalia, BisaBerlari):
    """LSP: Sapi tidak dipaksa terbang, hanya berlari"""
    def berlari(self):
        print(f"{self.nama} sedang berlari pelan.")

# Hewan air
class Ikan(Hewan, BisaBerenang):
    """ISP: Ikan tidak dipaksa terbang, hanya berenang"""
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Penyu(Hewan, BisaBerenang):
    """ISP: Penyu tidak dipaksa terbang, hanya berenang"""
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def berenang(self):
        print(f"{self.nama} sedang berenang pelan.")