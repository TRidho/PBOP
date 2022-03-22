#5210411225 SHEDY FACHRIAN MAULANA
#5210411226 DILAN NANDA PRATAMA
#5210411236 TABIA HANURAL
#5210411208 MUHAMMAD TAUFIK RIDHO

#Program Kalkulator Sederhana
class Kalkulator:
    def __init__(self,x,y):
        self.A = x
        self.B = y
        print("A = " +str(x)+", B = " +str(y))

class tambah(Kalkulator):
    def my_method(self):
        self.hasil = self.A+self.B
        print("A + B = " +str(self.hasil))

class kurang(Kalkulator):
    def my_method(self):
        self.hasil = self.A-self.B
        print("A - B = " +str(self.hasil))

class kali(Kalkulator):
    def my_method(self):
        self.hasil = self.A*self.B
        print("A * B = " +str(self.hasil))

class bagi(Kalkulator):
    def my_method(self):
        if self.B == 0 :
            print("Pembagian Dengan Nol")
        else :
            self.hasil = self.A/self.B
            print("A / B = " +str(self.hasil))

while True:
    print("==================")
    print("Operasi Matematika")
    print("1) Jumlah  [+]")
    print("2) Kurang  [-]")
    print("3) Kali    [*]")
    print("4) Bagi    [/]")
    print("5) Selesai.")
    print("==================")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == '1':
        num1 = int(input("Masukkan bilangan pertama : "))
        num2 = int(input("Masukkan bilangan kedua   : "))
        object=tambah(num1,num2)
        object.my_method()
    elif pilihan == '2':
        num1 = int(input("Masukkan bilangan pertama : "))
        num2 = int(input("Masukkan bilangan kedua   : "))
        object=kurang(num1,num2)
        object.my_method()
    elif pilihan == '3':
        num1 = int(input("Masukkan bilangan pertama : "))
        num2 = int(input("Masukkan bilangan kedua   : "))
        object=kali(num1,num2)
        object.my_method()
    elif pilihan == '4':
        num1 = int(input("Masukkan bilangan pertama : "))
        num2 = int(input("Masukkan bilangan kedua   : "))
        object=bagi(num1,num2)
        object.my_method()
    else:
        print("Terimakasih")
        break

    lanjut = input("Lanjutkan menghitung ? y/n ")

    if lanjut == 'n':
        print("Terimakasih")
        break