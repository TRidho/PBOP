#5210411208_MUHAMMAD TAUFIK RIDHO
#1.using class
class Jerman:
    def ibukota(self):
        print("Berlin adalah ibukota negara Jerman")

class Jepang:
    def ibukota(self):
        print("Tokyo adalah ibukota negara Jepang")

negara1 = Jerman()
negara2 = Jepang()

for country in (negara1,negara2):
    country.ibukota()

#2.polymorphism dengan class
class Kucing:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("meow")

class Anjing:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("guk..guk..")

kucing = Kucing("Tom",3)
anjing = Anjing("Spike",4)

for hewan in (kucing,anjing):
    hewan.bersuara()

#3.polymorphism dengan inheritance
class Burung:
    def intro(self):
        print("Di dunia ini ada beberapa type berbeda dari spesies burung")

    def terbang(self):
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang")

class Elang(Burung):
    def terbang(self):
        print("Elang dapat terbang")

class BurungUnta(Burung):
    def terbang(self):
        print("Burung Unta tidak dapat terbang")

obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

obj_burung.intro()
obj_burung.terbang()

obj_elang.intro()
obj_elang.terbang()

obj_burung_unta.intro()
obj_burung_unta.terbang()

#4.implementasi kelas abstrak
from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling(self):
        return 4 * self.__sisi

class Persegi(Bentuk):
    def __init__(self,sisi):
        self.__sisi = sisi
    def luas(self):
        return self.__sisi * self.__sisi
    def keliling(self):
        return 4 * self.__sisi

persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())

#5.implementasi overloading class pegawai
class Pegawai:
    jumlah = 0

    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self):
        print("Total pegawai", Pegawai.jumlah)

    def tampilPegawai(self):
        print("Nama:", self.nama, ",Gaji:", self.gaji)

    #method overloading
    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak+istri
            print("Tunjangan anak + istri =", total)
        else:
            total = istri
            print("Tunjangan istri =", total)

#memanggil kelas
peg1 = Pegawai("Taufik",2000)
peg2 = Pegawai("Ridho",2000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500,2000) #overloading
peg2.tunjangan(2500)      #overloading

print("Total pegawai %d" % Pegawai.jumlah)
rataGaji=(peg1.gaji + peg2.gaji)/Pegawai.jumlah
print("Rata-rata gaji ="+str(rataGaji))

#6.implementasi overriding class segiempat
class Segiempat():
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):  #method overriding
        print("Luas Segiempat =",self.panjang * self.lebar, "m^2")

class Bujursangkar(Segiempat):
    def __init__(self,sisi):
        self.side = sisi
        Segiempat.__init__(self,sisi,sisi)

    def hiutngLuas(self):  #method overriding
        print("Luas Bujur Sangkar =", self.side * self.side, "m^2")

b=Bujursangkar(4)
s=Segiempat(2,4)
b.hitungLuas()
s.hitungLuas()

#7.implementasi overloading
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def tampilMhs(self):
        print("Nama:", self.nama, "Nim:", self.nim)

    #method overloading
    def hitungSKS(self,jmlsks=None,sks=None):
        if jmlsks != None and sks !=None:
            totalsks = jmlsks + sks
            print("Total sks =",totalsks)
        else:
            totalsks = jmlsks
            print("Total sks =", totalsks)

#memangil kelas
mhs1 = Mahasiswa("Taufik",123180015)
mhs2 = Mahasiswa("Ridho",123180007)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80,34)  #overloading
mhs2.hitungSKS(83)     #overloading

#8.latihan mahasiswa overloading dan overriding
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def tampilMhs(self):
        print("Nama:", self.nama, "Nim:", self.nim)

    #method overloading
    def hitungSKS(self,jmlsks=None,sks=None):
        if jmlsks != None and sks !=None:
            totalsks = jmlsks + sks
            print("Total sks =",totalsks)
        else:
            totalsks = jmlsks
            print("Total sks =", totalsks)

        if totalsks>=100:
            print("Diperbolehkan mengambil skripsi")
        else:
            print("Tidak diperbolehkan mengambil skripsi")

    #method overriding
class Status(Mahasiswa):
    def __init__(self, nama, nim, status):
        self.nama = nama
        self.nim = nim
        self.status = status

    def tampilMhs(self):
        print("Nama:", self.nama, "Nim:", self.nim, ", Status Mahasiswa:",self.status)

#memangil kelas
mhs1 = Status("Taufik",123180015,"Aktif")
mhs2 = Status("Ridho",123180007,"Tidak Aktif")
mhs1.tampilMhs()
mhs1.hitungSKS(80,34)  #overloading
mhs2.tampilMhs()
mhs2.hitungSKS(83)     #overloading

#9.overloading class computer part
class ComputerPart:
    def __init__(self, pabrikan, jenis, harga):
        self.pabrikan=pabrikan
        self.jenis=jenis
        self.harga=harga

    def data(self):
        print('Pabrikan :',self.pabrikan, 'Jenis :',self.jenis,', Harga :',self.harga)

    def stok(self,stok):
        if stok >= 5:
            print("Ready ")
        else:
            print("Terbatas")

cp1=ComputerPart('Intel','Core i7 7740X',4350000)
cp1.data()
cp1.stok(6)
print()
cp2=ComputerPart('V-Gen','DDR4 SODimm PC19200/2400MHz',328000)
cp2.data()
cp2.stok(6)
print()
cp3=ComputerPart('Seagate','HDD 2.5 inch',295000)
cp3.data()
cp3.stok(4)
print()

#10.overriding class computer part
class ComputerPart:
    def __init__(self, pabrikan, jenis, harga):
        self.pabrikan=pabrikan
        self.jenis=jenis
        self.harga=harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, jenis, harga):
        self.pabrikan=pabrikan
        self.jenis=jenis
        self.harga=harga

    def data(self):
        print('Pabrikan :',self.pabrikan, 'Jenis :',self.jenis, 'Harga :',self.harga)

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, jenis, harga):
        self.pabrikan=pabrikan
        self.jenis=jenis
        self.harga=harga

    def data(self):
        print('Pabrikan :',self.pabrikan, 'Jenis :',self.jenis, 'Harga :',self.harga)


class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, jenis, harga):
        self.pabrikan=pabrikan
        self.jenis=jenis
        self.harga=harga

    def data(self):
        print('Pabrikan :',self.pabrikan, 'Jenis :',self.jenis, 'Harga :',self.harga)

p=Processor('Intel','Core i7 7740X',4350000)
p.data()
m=RandomAccessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz',328000)
m.data()
hdd=HardDiskSATA('Seagate','HDD 2.5 inch',295000)
hdd.data()