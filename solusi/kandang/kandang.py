# kandang.py
# Class Kandang - solusi SRP + DIP
# Dikerjakan oleh: Vicko

from abc import ABC, abstractmethod
from hewan.hewan import Hewan

# SOLUSI DIP - abstraksi untuk Kandang
class KandangBase(ABC):
    """Interface/abstraksi untuk semua jenis kandang"""
    @abstractmethod
    def tambah_hewan(self, hewan: Hewan):
        pass 
    @abstractmethod
    def get_semua_hewan(self):
        pass
        
    @abstractmethod
    def bersihkan_kandang(self):
        pass

# SOLUSI SRP - Kandang hanya bertanggung jawab
# menyimpan hewan dan membersihkan kandang
class Kandang(KandangBase):
    """Kandang konkret inherit KandangBase (DIP)
       Hanya bertanggung jawab menyimpan hewan (SRP)"""
    def __init__(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []

    def tambah_hewan(self, hewan: Hewan):
        self.hewan_list.append(hewan)
        print(f"{hewan.nama} ditambahkan ke {self.nama_kandang}.")

    def get_semua_hewan(self):
        return self.hewan_list

    def bersihkan_kandang(self):
        print(f"{self.nama_kandang} telah dibersihkan.")

    def __str__(self):
        return self.nama_kandang
