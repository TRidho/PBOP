#5210411208_MUHAMMAD TAUFIK RIDHO
#contoh Program
class Titik:
    def __init__(self,x,y):
        self.x = x
        self.y = y

titik_a = Titik(0,0)
titik_b = Titik(3,4)
print('Titik A Memiliki Koordinat ({},{})'.format(titik_a.x,titik_a.y))
print('Titik B Memiliki Koordinat ({},{})'.format(titik_b.x,titik_b.y))

#latihan
#class menu minuman
class MenuMinuman:
    def  __init__ (self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

mnm1 = MenuMinuman( 'Jus Jambu','Jus jambu merah tanpa gula',8560)
mnm2 = MenuMinuman( 'Jus Alpukat Ori','Jus alpukat dengan tambahan air gula merah',15000)
mnm3 = MenuMinuman( 'Jus Alpukat Xtra k','Jus alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000)
mnm4 = MenuMinuman( 'Red & Smooth', 'Smoothie pisang susu dengan strawberry',17500)

pilihan_minuman = (mnm1,mnm2,mnm3,mnm4)
print( 'Daftar menu Healthy Fruits')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'.format(mn.nama,mn.harga,mn.deskripsi)
    print(t)

#class buku
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul =judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku = Buku('Tenggelamnya Kapal Van der Wijck','HAMKA',1938)
t = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
print(t) 

#class garis
class Titik:
    def __init__(self,x,y):
        self.x = x
        self.x = y

class Garis:
    def __init__(self,titik_pertama,titik_kedua):
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua

def panjang(self):
    pjg_x = self.titik_kedua.x = self.titik_pertama.x
    pjg_y = self.titik_kedua.y = self.titik_pertama.y
    pjg = (pjg_x**2 + pjg_y**2)** 0.5
    return pjg
titik_a = Titik(0,0)
titik_b = Titik(3,4)
garis_ab = Garis(titik_a,titik_b)
print('panjang garis ab adalah {}'.format(garis_ab.panjang()))

#class mahasiswa 
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin','10120371"','Sistem Informasi',2020)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)