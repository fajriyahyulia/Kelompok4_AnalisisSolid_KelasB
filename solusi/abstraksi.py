# abstraksi.py
# Berisi semua base class dan interface
# Dibuat oleh: Fajriyah

from abc import ABC, abstractmethod

# ============================================
# BASE CLASS UTAMA
# ============================================
class HewanBase(ABC):
    """Base class untuk semua hewan"""
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    @abstractmethod
    def makan(self):
        pass

    def __str__(self):
        return f"{self.nama} dari {self.asal}"

# ============================================
# INTERFACE KEMAMPUAN
# ============================================
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

# ============================================
# MIDDLE CLASS - INHERITANCE BERTINGKAT
# ============================================
class Unggas(HewanBase):
    """Semua jenis unggas - inherit HewanBase"""
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

class Mamalia(HewanBase):
    """Semua jenis mamalia - inherit HewanBase"""
    def makan(self):
        print(f"{self.nama} sedang makan daging/rumput.")

class IkanBase(HewanBase):
    """Semua jenis ikan - inherit HewanBase"""
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")

# ============================================
# INTERFACE KANDANG
# ============================================
class KandangBase(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan: HewanBase):
        pass

    @abstractmethod
    def get_semua_hewan(self):
        pass

    @abstractmethod
    def bersihkan_kandang(self):
        pass