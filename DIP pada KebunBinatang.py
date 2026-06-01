from abc import ABC, abstractmethod

class IKandang(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass

    @abstractmethod
    def ambil_semua_hewan(self):
        pass


class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")


class Kandang(IKandang):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def ambil_semua_hewan(self):
        return self.hewan_list

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


class KebunBinatang:
    def __init__(self, kandang: IKandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.ambil_semua_hewan():
            hewan.makan()
            hewan.terbang()


kandang = Kandang()

burung = Hewan("Elang", "Burung")
kandang.tambah_hewan(burung)

kebun_binatang = KebunBinatang(kandang)
kebun_binatang.rawat_semua_hewan()