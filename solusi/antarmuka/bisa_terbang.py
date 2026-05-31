# bisa_terbang.py
# Interface untuk hewan yang bisa terbang
# Bagian dari solusi ISP

from abc import ABC, abstractmethod

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass