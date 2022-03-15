#1contoh program singel inheritance
#parent class
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

#child class mewarisi class hewan
class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong')

#objek
k=Kucing()
k.suara()
k.bersuara()

#2contoh program multilevel inheritance
#parent class
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

#child class mewarisi class hewan
class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong')

#child class anak kucing mewarisi dari class hewan
class AnakKucing(Kucing):
    def minum(self):
        print('minum susu')

#objek
ak=AnakKucing()
ak.bersuara()
ak.suara()
ak.minum()

#latihan program
#3contoh program hierarchial inheritance
#class parent
class Induk:
    def fungsiinduk(self):
        print('fungsi pada parent class')

#class turunan 1
class Anak1(Induk):
    def fungsianak1(self):
        print('fungsi pada anak 1')

#class turunan 2
class Anak2(Induk):
    def fungsianak2(delf):
        print('fugnsi pada anak 2')

#objek
a1=Anak1()
a2=Anak2()

a1.fungsiinduk()
a1.fungsianak1()

a2.fungsiinduk()
a2.fungsianak2()

#4contoh program multiple inheritance
#parent1
class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b

#parent2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b

#child
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b

#objek
h=Hitung()
print(h.penjumlahan(20,30))
print(h.perkalian(5,4))
print(h.pembagian(6,12))

#5kode program class computerpart
class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan=pabrikan
        self.nama=nama
        self.jenis=jenis
        self.harga=harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core=jumlah_core
        self.speed=speed

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas=kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, "SATA", harga)
        self.kapasitas=kapasitas
        self.rpm=rpm

p=Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
m=RandomAccessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
hdd=HardDiskSATA('Seagate','HDD 2.5 inch',295000,'500GB',7200)

parts=[p,m,hdd]
for part in parts:
    print('{} {} produksi {}'.format(part.jenis,part.nama,part.pabrikan))


#6single Inheritance
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def detailMhs(self):
        return self.nim, self.nama

    def cekMhs(self):
        if self.nim < 150000:
            return "Mahasiswa Aktif"
        else:
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa):
    def End(self):
        print("Mahasiswa Belum Melakukan Daftar Ulang")

mahasiswa1 = Mahasiswa('Mahasiswa 1', 135103)
print(mahasiswa1.detailMhs(), mahasiswa1.cekMhs())
mahasiswa2 = Siswa('Mahasiswa 2', 150503)
print(mahasiswa2.detailMhs(), mahasiswa2.cekMhs())
mahasiswa2.End()

#7multilevel inheritance
class Mahasiswa():
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa1(Mahasiswa):
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa2(Siswa1):
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

mhs1=Mahasiswa('Muhammad',135105)
mhs2=Siswa1('Taufik',13511)
mhs3=Siswa2('Ridho',134079)

print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)

#8hierarchical inheritance
class Mahasiswa():
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama=nama
        self.nim=nim

    def detSiswa1(self):
        print(self.nama,'alamat : Jogja')

class Siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama=nama
        self.nim=nim

    def detSiswa2(self):
        print(self.nama,'jurusan : informatika')

mhs1=Siswa1('Taufik',135105)
mhs2=Siswa2('Ridho',135117)

print(mhs1.nim)
mhs1.detSiswa1()
print(mhs2.nim)
mhs2.detSiswa2()

#9multiple inheritance
class Mahasiswa1():
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Mahasiswa2():
    def __init__(self,alamat,jurusan):
        self.alamat=alamat
        self.jurusan=jurusan

class Siswa(Mahasiswa1,Mahasiswa2):
    def __init__(self, nama, nim, alamat, jurusan):
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self,alamat,jurusan)

s=Siswa('Taufik',135105,'Jogja','informatika')
print('nim',s.nim, 'nama',s.nama, 'alamat',s.alamat, 'jurusan',s.jurusan)

#tugas
#10multilevel inheritance
class ComputerPart:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Storage(ComputerPart):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)
        self.jenis = jenis

class Harddisk(Storage):
    def __init__(self,nama, harga, kapasistas):
        super().__init__(nama, harga, 'HDD')
        self.kapasitas = kapasistas

pc = Harddisk('Samsung Internal Hardisk', 750000, '1 TB')

print(f'Computer dengan penyimpanan jenis {pc.jenis} {pc.nama} dengan harga {pc.harga} berkapasitas {pc.kapasitas}')

#11hierarchical inheritance
class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan=pabrikan
        self.nama=nama
        self.jenis=jenis
        self.harga=harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core=jumlah_core
        self.speed=speed

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas=kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, "SATA", harga)
        self.kapasitas=kapasitas
        self.rpm=rpm

p=Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
m=RandomAccessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
hdd=HardDiskSATA('Seagate','HDD 2.5 inch',295000,'500GB',7200)

parts=[p,m,hdd]
for part in parts:
    print('{} {} produksi {}'.format(part.jenis ,part.nama, part.pabrikan))

#12multiple inheritance
class prosessor() :
    def __init__(self, prosesor) -> None:
        self.prosesor = prosesor

class RandomAccsesmemori() :
    def __init__(self, detail_ram) -> None:
        self.ram = detail_ram

class Storage() :
    def __init__(self, hdd) -> None:
        self.hdd = hdd

class Monitor() :
    def __init__(self, mntr) -> None:
        self.monitor = mntr

class Computerpart(prosessor, Storage, RandomAccsesmemori, Monitor) :
    def __init__(self, prosesor, ram, hdd, mntr) -> None:
        prosessor.__init__(self, prosesor)
        Storage.__init__(self, hdd)
        RandomAccsesmemori.__init__(self, ram)
        Monitor.__init__(self, mntr)

this_pc = Computerpart('Intel Core i5', 'RAM 16GB DDR4', 'HDD1 TB', '24 inch')
print(f'contoh komputer dengan Processor {this_pc.prosesor} Random Acces Memory {this_pc.ram} Storage {this_pc.hdd} Monitor{this_pc.monitor}')