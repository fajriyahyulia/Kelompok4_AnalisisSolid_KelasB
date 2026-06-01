# hewan_solusi.py
# Analisis: SRP + ISP pada class Hewan
# Dikerjakan oleh: Fatimah

from abc import ABC, abstractmethod

# ============================================
# ANALISIS PELANGGARAN
# ============================================
# SRP: Class Hewan punya 2 tanggung jawab:
#      1. Menyimpan data (nama, jenis)
#      2. Mendefinisikan perilaku (makan, terbang)
# ISP: Semua hewan dipaksa punya method terbang()
#      padahal tidak semua hewan bisa terbang
# ============================================

# SOLUSI ISP - pisah interface sesuai kemampuan
class BisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

class BisaBerlari(ABC):
    @abstractmethod
    def berlari(self):
        pass

# SOLUSI SRP - class Hewan hanya menyimpan data
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def __str__(self):
        return f"{self.nama} ({self.jenis})"

# Subclass implement interface sesuai kemampuan masing-masing
class Burung(Hewan, BisaMakan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Ikan(Hewan, BisaMakan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class Kucing(Hewan, BisaMakan, BisaBerlari):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")