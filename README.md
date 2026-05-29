# Kelompok 4 - Analisis Prinsip SOLID

## Anggota & Pembagian Tugas
| Nama | Branch | Tugas |
|------|--------|-------|
| Fajriya (Ketua) | main | Setup repo, integrasi, README |
| Fatimah | fatimah-hewan-srp-isp | Analisis & solusi SRP + ISP pada class Hewan |
| Rahma | rahma-hewan-lsp | Solusi LSP + subclass Burung, Ikan, dll |
| Viko | viko-kandang-srp-dip | Analisis & solusi SRP + DIP pada class Kandang |
| Wijang | wijang-kebunbinatang-ocp | Analisis & solusi OCP pada KebunBinatang |
| Abid | abid-kebunbinatang-dip | Solusi DIP pada KebunBinatang |

---

## Analisis Prinsip SOLID pada Kode Awal

### Kode Awal (Sebelum Diperbaiki)
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

## Prinsip SOLID yang Dilanggar

### ❌ 1. SRP - Single Responsibility Principle (Dilanggar)
**Prinsip:** Setiap class hanya boleh punya satu tanggung jawab.

**Pelanggaran pada class `Hewan`:**
- Class `Hewan` punya dua tanggung jawab sekaligus: menyimpan data hewan (`nama`, `jenis`) dan mendefinisikan perilaku hewan (`makan`, `terbang`).
- Method `terbang()` tidak relevan untuk semua jenis hewan (contoh: ikan tidak bisa terbang).

**Pelanggaran pada class `Kandang`:**
- Class `Kandang` bertanggung jawab menyimpan daftar hewan sekaligus membersihkan kandang.

---

### ❌ 2. OCP - Open/Closed Principle (Dilanggar)
**Prinsip:** Class terbuka untuk ekstensi, tertutup untuk modifikasi.

**Pelanggaran pada class `KebunBinatang`:**
- Method `rawat_semua_hewan()` langsung memanggil `hewan.terbang()` untuk semua hewan.
- Jika ada hewan baru yang tidak bisa terbang, kita harus **mengubah** kode `KebunBinatang`, bukan hanya menambah class baru.

---

### ❌ 3. LSP - Liskov Substitution Principle (Dilanggar)
**Prinsip:** Subclass harus bisa menggantikan parent class tanpa merusak program.

**Pelanggaran:**
- Jika dibuat subclass `Ikan(Hewan)`, method `terbang()` tetap ada padahal ikan tidak bisa terbang.
- Memanggil `ikan.terbang()` akan menghasilkan perilaku yang tidak masuk akal.

---

### ❌ 4. ISP - Interface Segregation Principle (Dilanggar)
**Prinsip:** Class tidak boleh dipaksa mengimplementasi method yang tidak dibutuhkan.

**Pelanggaran:**
- Semua hewan "dipaksa" punya method `terbang()` padahal tidak semua hewan bisa terbang.
- Seharusnya kemampuan terbang dipisah ke interface/class tersendiri.

---

### ❌ 5. DIP - Dependency Inversion Principle (Dilanggar)
**Prinsip:** Class tingkat tinggi tidak boleh bergantung langsung ke class tingkat rendah, tapi ke abstraksi.

**Pelanggaran pada class `KebunBinatang`:**
- `KebunBinatang` langsung membuat objek `Kandang()` di dalam `__init__`.
- Ini membuat `KebunBinatang` sangat bergantung ke class `Kandang` secara langsung.

---

## Kesimpulan

| Prinsip | Status | Keterangan |
|---------|--------|------------|
| SRP | ❌ Dilanggar | Class Hewan & Kandang punya lebih dari 1 tanggung jawab |
| OCP | ❌ Dilanggar | KebunBinatang harus diubah jika ada hewan baru |
| LSP | ❌ Dilanggar | Subclass Ikan tidak cocok dengan method terbang() |
| ISP | ❌ Dilanggar | Semua hewan dipaksa punya method terbang() |
| DIP | ❌ Dilanggar | KebunBinatang bergantung langsung ke class Kandang |

**Kesimpulan: Kode awal tidak memenuhi satupun prinsip SOLID dan perlu diperbaiki seluruhnya.**

---

## Struktur File
- `hewan.py` - Kode awal sebelum SOLID
- `solusi/` - Folder kode setelah diperbaiki tiap anggota