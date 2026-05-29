# kandang_solusi.py
# Analisis: SRP + DIP pada class Kandang
# Dikerjakan oleh: Viko

from abc import ABC, abstractmethod

# SRP - pisah tanggung jawab Kandang
# DIP - buat abstraksi untuk Kandang

class IKandang(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def get_hewan_list(self):
        pass

class Kandang(IKandang):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def get_hewan_list(self):
        return self.hewan_list

# SRP - tanggung jawab bersihkan kandang dipisah
class PetugasKebersihan:
    def bersihkan_kandang(self, kandang: IKandang):
        print("Kandang dibersihkan.")