# kebunbinatang_solusi.py
# Analisis: OCP + DIP pada class KebunBinatang
# Dikerjakan oleh: Wijang (OCP) & Abid (DIP)

from abc import ABC, abstractmethod

# DIP - KebunBinatang bergantung ke abstraksi, bukan class langsung
class IKandang(ABC):
    @abstractmethod
    def get_hewan_list(self):
        pass

# OCP - KebunBinatang tidak perlu diubah jika ada hewan baru
class KebunBinatang:
    def __init__(self, kandang: IKandang):  # DIP - inject lewat parameter
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_hewan_list():
            hewan.makan()  # OCP - cukup panggil makan(), tidak paksa terbang()