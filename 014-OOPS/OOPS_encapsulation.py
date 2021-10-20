# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'Setia Sejati'
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan +=insentif_proyek
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
    # Buat fungsi untuk bisa menampilkan private modifier
    def tampilkan_nama(self):
        print(budi.__nama)

# Buat objek karyawan
budi = Karyawan('Budi', 25, 8500000)

# Akses ke attribute class Karyawan
print(budi.__class__.nama_perusahaan)

# Akses nama dari class Karyawan
budi.tampilkan_nama()
