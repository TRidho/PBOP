#5210411208_Muhammad Taufik Ridho
#tugas week 3 class python
#class menu minuman
class MenuMinuman:
    def  __init__ (self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

mnm1 = MenuMinuman( 'Jus Jambu','Jus jambu merah tanpa gula',8560)
mnm2 = MenuMinuman( 'Jus Alpukat Ori','Jus alpukat dengan tambahan air gula merah',15000)
mnm3 = MenuMinuman( 'Jus Alpukat Xtra k','Jus alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000)
mnm4 = MenuMinuman( 'Jus Mangga','Jus mangga ',17500)
mnm5 = MenuMinuman( 'Jus Tomat','Jus Tomat dengan tambahan gula',8500)
mnm6 = MenuMinuman( 'Red & Smooth', 'Smoothie pisang susu dengan strawberry',17500)

pilihan_minuman = (mnm1,mnm2,mnm3,mnm4)
print( 'Daftar menu Healthy Fruits :')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'.format(mn.nama,mn.harga,mn.deskripsi)
    print(t)

#class mahasiswa 
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020)
m2 = Mahasiswa('Ridho','10120452','Informatika',2020)
m3 = Mahasiswa('Taufik','10120210','Arsitektur',2020)

pilih_mahasiswa = (m1,m2,m3)
print( 'Daftar Mahasiswa :')
for m in pilih_mahasiswa:
    teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(m.nama,m.prodi,m.thn_masuk,m.nim)
    print(teks)

#class buku
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul =judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku('Tenggelamnya Kapal Van der Wijck','HAMKA',1938)
buku2 = Buku('Laskar Pelangi','Andrea Hirata',2005)

pilihan_buku = (buku1,buku2)
print( 'Daftar Buku :')
for buku in pilihan_buku:
    t = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
    print(t)