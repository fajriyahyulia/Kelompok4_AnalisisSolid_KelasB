# Kelompok 4 - Analisis Prinsip SOLID

Proyek ini merupakan latihan analisis dan penerapan prinsip SOLID pada kode Python sederhana tentang sistem kebun binatang.

---

## Anggota & Pembagian Tugas

| Nama | Branch | Tugas |
|------|--------|-------|
| Fajriya (Ketua) | main | Setup repo, integrasi, README |
| Fatimah | fatimah-hewan-srp-isp | Analisis & solusi SRP + ISP pada class Hewan |
| Rahma | rahma-hewan-lsp | Analisis & solusi LSP + subclass hewan |
| Viko | viko-kandang-srp-dip | Analisis & solusi SRP + DIP pada class Kandang |
| Wijang | wijang-kebunbinatang-ocp | Analisis & solusi OCP pada KebunBinatang |
| Abid | abid-kebunbinatang-dip | Analisis & solusi DIP pada KebunBinatang |

---

## Struktur Folder

```
Kelompok4_AnalisisSolid_KelasB/
├── hewan.py              
├── README.md             
└── solusi/
    ├── antarmuka/
    │   ├── bisa_terbang.py
    │   ├── bisa_berenang.py
    │   └── bisa_berlari.py
    ├── hewan/
    │   ├── hewan.py
    │   ├── hewan_darat.py
    │   └── hewan_terbang.py
    ├── kandang/
    │   └── kandang.py
    ├── layanan/
    │   ├── perawatan.py
    │   └── pemberian_makan.py
    ├── kebun_binatang/
    │   └── kebun_binatang.py
    └── main.py
```

---

## Kode Awal (Sebelum Diperbaiki)

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def makan(self):
        print(f"{self.nama} sedang makan.")
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
```

---

## Analisis Pelanggaran SOLID

### 1. SRP - Single Responsibility Principle
**Pelanggaran:**
- Class `Hewan` punya dua tanggung jawab: menyimpan data sekaligus mendefinisikan perilaku hewan.
- Method `terbang()` tidak relevan untuk semua jenis hewan, seperti ikan atau sapi.

**Solusi:** Pisahkan data hewan ke `Hewan` (base class), perilaku ke subclass masing-masing, dan tanggung jawab pembersihan kandang ke class `Perawatan` tersendiri.

---

### 2. OCP - Open/Closed Principle
**Pelanggaran:**
- Method `rawat_semua_hewan()` selalu memanggil `hewan.terbang()` untuk semua hewan tanpa terkecuali.
- Jika ingin menambah hewan baru, kita terpaksa mengubah kode yang sudah ada.

**Solusi:** Gunakan `isinstance` check sehingga `KebunBinatang` tidak perlu diubah jika ada hewan atau kemampuan baru.

---

### 3. LSP - Liskov Substitution Principle
**Pelanggaran:**
- Jika dibuat subclass `Sapi(Hewan)`, method `terbang()` tetap ada padahal sapi tidak bisa terbang.
- Memanggil `sapi.terbang()` menghasilkan perilaku yang tidak logis.

**Solusi:** Setiap subclass hanya implement kemampuan yang sesuai, sehingga bisa menggantikan parent class tanpa merusak logika program.

---

### 4. ISP - Interface Segregation Principle
**Pelanggaran:**
- Semua hewan dipaksa punya method `terbang()` padahal tidak semua bisa terbang.

**Solusi:** Pisahkan interface menjadi `BisaTerbang`, `BisaBerenang`, dan `BisaBerlari` sehingga hewan hanya implement yang sesuai.

---

### 5. DIP - Dependency Inversion Principle
**Pelanggaran:**
- `KebunBinatang` langsung membuat objek `Kandang()` di dalam constructor.
- Bergantung ke class konkret, bukan abstraksi.

**Solusi:** Buat abstraksi `KandangBase` dan inject `Kandang` lewat parameter constructor.

---

## Kesimpulan

| Prinsip | Status Awal | Setelah Diperbaiki |
|---------|-------------|-------------------|
| SRP |  Dilanggar | ✅ Tiap class punya 1 tanggung jawab |
| OCP |  Dilanggar | ✅ Pakai isinstance, tidak perlu ubah kode |
| LSP |  Dilanggar | ✅ Subclass hanya implement kemampuan sesuai |
| ISP |  Dilanggar | ✅ Interface dipisah per kemampuan |
| DIP |  Dilanggar | ✅ Bergantung ke abstraksi KandangBase |

---

## Cara Menjalankan

```bash
cd solusi
python main.py
```

---

## Link Repository

https://github.com/fajriyahyulia/Kelompok4_AnalisisSolid_KelasB
