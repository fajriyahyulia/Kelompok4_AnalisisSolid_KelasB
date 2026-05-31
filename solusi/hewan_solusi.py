# hewan_solusi.py
# Analisis: SRP + ISP + LSP pada class Hewan
# Dikerjakan oleh: Fatimah (SRP+ISP) & Rahma (LSP)

from abstraksi import Unggas, Mamalia, IkanBase, BisaTerbang, BisaBerenang, BisaBerlari

# ============================================
# FATIMAH - SRP + ISP
# ============================================
# SRP: HewanBase hanya simpan data
#      Unggas, Mamalia, IkanBase handle perilaku
# ISP: Interface dipisah sesuai kemampuan
#      BisaTerbang, BisaBerenang, BisaBerlari
# ============================================

# Unggas yang bisa terbang
class Elang(Unggas, BisaTerbang):
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

# Unggas yang tidak bisa terbang
class Ayam(Unggas, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

# Mamalia yang bisa berlari
class Singa(Mamalia, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari kencang.")

# Ikan yang bisa berenang
class Ikan(IkanBase, BisaBerenang):
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

# ============================================
# RAHMA - LSP
# ============================================
# LSP: Setiap subclass bisa menggantikan
#      parent class tanpa merusak program.
#      Subclass hanya implement kemampuan
#      yang sesuai dengan hewannya.
# ============================================

# Unggas yang bisa terbang dan berenang
class Bebek(Unggas, BisaTerbang, BisaBerenang):
    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

# Mamalia yang hanya makan
class Sapi(Mamalia, BisaBerlari):
    def berlari(self):
        print(f"{self.nama} sedang berlari pelan.")

# Ikan yang berenang pelan
class Penyu(IkanBase, BisaBerenang):
    def berenang(self):
        print(f"{self.nama} sedang berenang pelan.")

# Unggas yang bisa terbang
class Burung(Unggas, BisaTerbang):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")