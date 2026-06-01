#Analisis Sebelum DIP
class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()
#Class KebunBinatang bergantung langsung pada class Kandang
#Sulit diperluas jika ada jenis kandang lain


#Analisis Setelah DIP
class KebunBinatang:
    def __init__(self, kandang: IKandang):
        self.kandang = kandang
#Class KebunBinatang hanya bergantung pada abstraksi IKandang
#Implementasi kandang dapat diganti tanpa mengubah kode class KebunBinatang
#Kode menjadi lebih fleksibel, mudah diuji, dan sesuai dengan prinsip DIP