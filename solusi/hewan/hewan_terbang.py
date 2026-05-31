# hewan_terbang.py
# Subclass untuk hewan yang bisa terbang dan berenang
# Bagian dari solusi LSP

from hewan.hewan_darat import Unggas, Mamalia
from hewan.hewan import Hewan
from antarmuka.bisa_terbang import BisaTerbang
from antarmuka.bisa_berenang import BisaBerenang
from antarmuka.bisa_berlari import BisaBerlari

# Unggas yang bisa terbang
class Elang(Unggas, BisaTerbang):
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

class Burung(Unggas, BisaTerbang):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Ayam(Unggas, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

# Unggas yang bisa terbang dan berenang
class Bebek(Unggas, BisaTerbang, BisaBerenang):
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

# Mamalia
class Singa(Mamalia, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari kencang.")

class Sapi(Mamalia, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari pelan.")

# Hewan air
class Ikan(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Penyu(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def berenang(self):
        print(f"{self.nama} sedang berenang pelan.")