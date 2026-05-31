# abstraksi.py
# Berisi semua base class dan interface
# Dibuat oleh: Fajriya (Ketua)

from abc import ABC, abstractmethod

# Base class untuk semua hewan
class HewanBase(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

# Interface kemampuan hewan
class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

# Interface untuk kandang
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