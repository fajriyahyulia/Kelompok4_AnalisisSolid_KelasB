# bisa_berenang.py
# Interface untuk hewan yang bisa berenang
# Bagian dari solusi ISP

from abc import ABC, abstractmethod

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass