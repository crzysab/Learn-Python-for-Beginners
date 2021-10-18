# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'Setia Sejati'

# Inisiasi object yang dinyatakan dalam variabel
budi = Karyawan()
siti = Karyawan()

# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(budi.__class__.nama_perusahaan)

# Ubah nama_perusahaan
budi.__class__.nama_perusahaan = 'Permata'
# Cetak nama_perusahaan objek
print(budi.__class__.nama_perusahaan)
print(siti.__class__.nama_perusahaan)