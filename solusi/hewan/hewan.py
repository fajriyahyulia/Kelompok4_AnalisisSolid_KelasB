# hewan.py
# Base class untuk semua hewan
# Bagian dari solusi SRP

from abc import ABC, abstractmethod

class Hewan(ABC):
    """Base class untuk semua hewan (SRP - hanya simpan data)"""
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    @abstractmethod
    def makan(self):
        pass

    def __str__(self):
        return f"{self.nama} dari {self.asal}"