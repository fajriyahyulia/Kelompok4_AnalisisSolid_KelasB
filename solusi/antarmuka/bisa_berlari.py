# bisa_berlari.py
# Interface untuk hewan yang bisa berlari
# Bagian dari solusi ISP

from abc import ABC, abstractmethod

class BisaBerlari(ABC):
    @abstractmethod
    def berlari(self):
        pass