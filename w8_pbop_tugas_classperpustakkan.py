from ast import Break
import csv
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

def main_menu():
    while(True):
        print("\nMenu PerpustakaanPerpustakaan")
        print("1. Mencari Buku")
        print("2. Mencari Majalah")
        print("3. Mencari DVD")
        print("4. List Buku")
        print("5. Selesai")
        try:
            menu = int(input("Input pilihan menu yang ingin anda cari : "))
            print()
            if(menu == 1):
                Data_Buku()
                kembali()

            elif(menu == 2):
                Data_Majalah()
                kembali()

            elif(menu == 3):
                Data_DVD()
                kembali()

            elif(menu == 4):
                List_Buku()
                kembali()

            elif(menu == 5):
                Keluar()
                break

            else:
                print("Masukan pilihan menu yang anda inginkan")
                continue

        except ValueError:
            print("Input Salah!")
            continue

def Data_Buku():
    with open('Buku.txt') as temp_f:
        data_b = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari "))
    for b in data_b:
        if search in b:
            return True, print(b,"Buku yang anda cari tersedia")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def Data_Majalah():
    with open('stock.txt') as temp_f:
        data_m = temp_f.readlines()
        search = str(input("Masukkan judul Majalah yang anda ingin cari"))
    for m in data_m:
        if search in m:
            return True, print(m,"Majalah yang anda cari tersedia")
    return False, print("Maaf Majalah yang anda cari tidak tersedia")

def Data_DVD():
    with open('stock.txt') as temp_f:
        data_D = temp_f.readlines()
        search = str(input("Masukkan judul DVD yang anda ingin cari"))
    for D in data_D:
        if search in D:
            return True, print(D,"DVD yang anda cari tersedia")
    return False, print("Maaf DVD yang anda cari tidak tersedia")

def List_Buku():
    with open('stock.txt', 'r+') as f:
        list = f.read()
        print(list)
        print()

def Keluar():
    print("Terimakasih")

main_menu()