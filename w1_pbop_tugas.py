#5210411208_MUHAMMAD TAUFIK RIDHO
#Menghitung Luas dan Keliling Segitiga
while True :
    print("---Menu---")
    print("1.Menghitung Luas Segitiga.")
    print("2.Menghitung Keliling Segitiga.")
    print("0.Selesai.")
    pilih = input("Masukkan Pilihan : ")

    if pilih == '1':
        alas=float(input("Alas : "))
        tinggi=float(input("Tinggi : "))

        luas = 1/2*alas*tinggi
        print("Luas Segitiga =", luas)
    
    elif pilih == '2':
        s1=float(input("Sisi Pertama : "))
        s2=float(input("Sisi Kedua : "))
        s3=float(input("Sisi Ketiga : "))

        keliling = s1+s2+s3
        print("Luas Segitiga =", keliling)
    else:
        print('Terimakasih')
        break
