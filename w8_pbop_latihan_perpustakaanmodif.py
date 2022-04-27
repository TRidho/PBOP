import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)
cur=mydb.cursor()

class PerpusItem:
    def __init__(self,judul,subjek,lokasi):
        self.judul  = judul
        self.subjek = subjek
        self.lokasi = lokasi

class Buku(PerpusItem):
    def __init__(self,judul,subjek,lokasi,penerbit,tahunTerbit,jmlHal):
        super().__init__(judul,subjek,lokasi)
        self.penerbit    = penerbit
        self.tahunTerbit = tahunTerbit
        self.jmlHal      = jmlHal

class Majalah(PerpusItem):
    def __init__(self,judul,subjek,lokasi,volume,edisi):
        super().__init__(judul,subjek,lokasi)
        self.volume = volume
        self.edisi  = edisi

class DVD(PerpusItem):
    def __init__(self,judul,subjek,lokasi,aktor,genre):
        super().__init__(judul,subjek,lokasi)
        self.aktor = aktor
        self.genre = genre
while True:
    print("==================")
    print("Menu Perpustakaan")
    print("1) Buku")
    print("2) Majalah")
    print("3) DVD")
    print("4) Selesai.")
    print("==================")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == '1':
        book = [Buku(indeks[1],'Buku',indeks[2],indeks[3],indeks[4],indeks[5])]
        for dft in book:
            print("\nJudul : {}\nTipe : {}\nLokasi : {}\nPenerbit : {}\nTahun Terbit : {}\nJumlah Halaman: {}".format(dft.judul,dft.subjek,dft.lokasi,dft.penerbit,dft.tahunTerbit,dft.jmlHal))

    elif pilihan == '2':
        dvd = [DVD(indeks[1],"DVD",indeks[2],indeks[8],indeks[9])]
        for dft in dvd:
            print("\nJudul : {}\nTipe : {}\nLokasi : {}\nAktor : {}\nGenre : {}".format(dft.judul,dft.subjek,dft.lokasi,dft.aktor,dft.genre))

    elif pilihan == '3':
        magazine = [Majalah(indeks[1],'Majalah',indeks[2],indeks[6],indeks[7])]
        for dft in magazine:
            print("\nJudul : {}\nTipe : {}\nLokasi : {}\nVolume : {}\nEdisi : {}".format(dft.judul,dft.subjek,dft.lokasi,dft.volume,dft.edisi))

    else:
        print("Terimakasih")
        break

    lanjut = input("Lanjutkan mencari ? y/n ")

    if lanjut == 'n':
        print("Terimakasih")
        break