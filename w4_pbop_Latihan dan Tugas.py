#5210411208_Muhammad Taufik Ridho
#1 contoh program dengan hak akses public
class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitiga_besar = Segitiga(100,80)

print("alas : ", segitiga_besar.alas)
print("tinggi : ", segitiga_besar.tinggi)
print("luas : ", segitiga_besar.luas)

#2 contoh program dengan hak akses protected
class Utama:
    def __init__(self):
        self._a = 2

class Turunan(Utama):
    def __init__(self):
        #memanggil konstruktor pada kelas utama
        Utama.__init__(self)
        print("memanggil variabel protected pada class utama : ",self._a)

        #memodifikasi nila variabel protected
        self._a = 3
        print("memanggil variabel protected yang dimodifikasi diluar class : ", self._a)

objek1 = Turunan()
objek2 = Utama()

#memanggil variabel protected
print("mengakses variabel protected dari objek1 :",objek1._a)
print("mengakses variabel protected dari objek2 :",objek2._a)

#3 contoh program dengan hak akses private:
class Hitung:
    def __init__(self):
        self. __angkaRahasia=0

    def tampilkanHitung(self):
        self. __angkaRahasia +=1
        print(self. __angkaRahasia)

hitungan=Hitung()
hitungan.tampilkanHitung()

#latihan variabel dengan hak akses public, protected, dan privat
#4 semua variabel bersifat public
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.jendela=jendela
        self.pintu=pintu
        self.mesin=mesin

audi=Mobil(4,5,"Diesel")
print(audi.jendela)
print(audi.pintu)
print(audi.mesin)

#5 semua variabel bersifat protected
class Mobil :
    def __init__(self, jendela, pintu, mesin) :
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin

audi = Mobil(4, 4, "Disel")

class Truk(Mobil) :
    def __init__ (self, jendela, pintu, mesin, tipe) :
        super().__init__(jendela, pintu, mesin)
        self.tipebak = tipe

truk = Truk(4, 4, "Disel", "Bak Terbuka")
print(truk._mesin)
print(truk.tipebak)

#6 semua variabel bersifat privat
class Mobil() :
    def __init__(self, jendela, pintu, mesin) :
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin

    def Tampil(self) :
        print(f"Jendela : {self.__jendela}")
        print(f"Pintu : {self.__pintu}")
        print(f"Mesin : {self.__mesin}")

audi = Mobil(4,4,"Diesel")
audi.Tampil()

#7 fungsi private dan public
class Pegawai:
    __nama=""
    __alamat=""
    __gaji=0

    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat

    def __hitungGaji(self):
        upahLembur=20000
        gajiPokok=2000000
        jumLembur=int(input("Total jam lembur :"))
        self.__gaji=(upahLembur*jumLembur)+gajiPokok

    def tampilDetail(self):
        print("\n--Menghitung dan menampilkan detail gaji pegawai--")
        print("nama :", self.__nama)
        print("alamat :", self.__alamat)
        self.__hitungGaji()
        print("total gaji :", self.__gaji)

#membuat objek pegawai
pgw1=Pegawai("taufik","bengkulu")
pgw1.tampilDetail()

pgw2=Pegawai("ridho","jogja")
pgw2.tampilDetail()

#8 class menu minuman
class MenuMinuman:
    def  __init__ (self,nama,deskripsi,harga,stok):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")

mnm1 = MenuMinuman( 'Jus Jambu','Jus jambu merah tanpa gula',8560,50)
mnm2 = MenuMinuman( 'Jus Alpukat Ori','Jus alpukat dengan tambahan air gula merah',15000,30)
mnm3 = MenuMinuman( 'Jus Alpukat Xtra k','Jus alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000,40)
mnm4 = MenuMinuman( 'Jus Mangga','Jus mangga ',17500,30)
mnm5 = MenuMinuman( 'Jus Tomat','Jus Tomat dengan tambahan gula',8500,20)
mnm6 = MenuMinuman( 'Red & Smooth', 'Smoothie pisang susu dengan strawberry',17500,35)

pilihan_minuman = (mnm1,mnm2,mnm3,mnm4,mnm5,mnm6)
print( 'Daftar menu Healthy Fruits :')
for mn in pilihan_minuman:
    mn.Tampil()

#9 class mahasiswa
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk,status):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__status = status

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa berstatus {self.__status} prodi {self.prodi} dengan nim {self.nim}")

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,'tidak aktif')
m2 = Mahasiswa('Ridho','10120452','Informatika',2020,'aktif')
m3 = Mahasiswa('Taufik','10120210','Arsitektur',2020,'aktif')

pilih_mahasiswa = (m1,m2,m3)
print( 'Daftar Mahasiswa :')
for m in pilih_mahasiswa:
    m.Tampil()

#10 class buku
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit,stok):
        self.judul =judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__stok = stok

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah stok buku {self.__stok}\n")

buku1 = Buku('Tenggelamnya Kapal Van der Wijck','HAMKA',1938,40)
buku2 = Buku('Laskar Pelangi','Andrea Hirata',2005,200)

pilihan_buku = (buku1,buku2)
print( 'Daftar Buku :')
for buku in pilihan_buku:
    buku.Tampil()
