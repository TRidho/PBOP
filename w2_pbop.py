#5210411208_MUHAMMAD TAUFIK RIDHO

#1.print string
str='aku cinta Indonesia'
print(str)

#2.menambah diantara string
str=str[:10]+'tanah air ku'+str[9:]
print(str)

#3.menghapus string
str=''
print(str)

#4.menghapus string dengan indeks tertentu
str1='aku cinta tanah air ku Indonesia'
str1=str1[:9]+''+str1[22:]
print(str1)

#5.uppper dan lower case
kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)

#6.menghilangkan spasi awal dan akhir string
s='     python     '
a1=s.strip()
print(a1)
#menghilangkan spasi awal string
b1=s.lstrip()
print(b1)
#menghilangkan spasi akhir string
c1=s.rstrip()
print(c1)

#7.menghitung jumlah string
jumlah=len(kelas)
print('panjang string =', jumlah)

#8.menggabungkan string
s1='python'
s2='programming'
hasil=s1+s2
print(hasil)

#9.menetukan indeks
print(kelas.index('a'))

#10.mengganti kata 
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)

#11.menampilkan string yang terformat
a2='satu'
b2='dua'
c2='tiga'
print('saya mempunyai %s mangga' %(b2))

#12.membagi per srtring
a3=kelas2.split()
print(a3)

#13.input dari keyboard
print(input('hari ini adalah : '))

data1=input('angka 1:')
data2=input('angka 2:')
hasil=int(data1)*int(data2)
print(data1,'*',data2,'=',hasil)

#14.tipe data list
list=[0,1,2,3,4,5,6,7,8,9]
print(list)

#15.akses list indeks tertentu
print(list[0])

#16.menampilkan 3 data pertama pada list
print(list[:3])

#16.menampilkan 3 data terakhir pada list (harus mengetahui jumlah elemen pada list)
len(list)
#selanjutnya
print(list[10-3:])

#17.menampilkan beberapa data pada indeks tertentu
print(list[2:9])

#18.mengakses menggunakan indeks negatif
print(list[-10])

#19.menambah elemen baru di akhir list
list.append(10)
print(list)

#20.menambah elemen baru di indeks tertentu pada list
list.insert(1,11)
print(list)

#21.menggabungkan 2 list
list2=['halo']
list.extend(list2)
print(list)
list.extend('hai')
print(list)

#22.menghapus isi list
del list[1]
print(list)

list.remove(10) #langsung menghapus elemen yang tertulis menggunakan indeks
print(list)

list.pop() #mengambil elemen list terakhir
print(list)
list.pop(2) #menggunakan indeks
print(list)

#23.mengurutkan isi list
list3=[50,10,20,30,40]
print(list3)
urut=sorted(list3)
print(urut)
list3.sort()
print(list3)

#24.mengurutkan tebalik
list3.sort(reverse=True)
print(list3)

#25.mencari nilai terkecil dan terbesar
min(list3)
print(list3)

max(list3)
print(list3)

#26.dictionary
d={1:100,2:200,3:300,4:400,5:500}
print(d)

#27.mengakses dictionary
a4=d[2]
print(a4)

a5=d.get(4)
print(a5)

#28.mencari kunci
a6=d.keys()
print(a6)

#29.mencari nilai
a7=d.values()
print(a7)

#30.menghapus elemen tertentu
del d[1]

#31.copy
d.copy()

#32.tuple
t=(100,200,300,400)
print(t)

#33.mengakses tuple
t[3]

#34.mengetahui indeks
t.index(200)

#35.mencari banyak data yang sama
t2=(10,20,10,30,10,40,20)
print(t2)
t2.count(10)

#36.set
set={1,2,3}
print(set)
