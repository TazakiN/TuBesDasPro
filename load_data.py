# load_data.py
# File ini digunakan untuk meload semua data saat awal memulai program

#import
from util import *

# LOADING data dari file "user.csv" ke dalam Array of Array of String dengan nama variabel data_user
user = open("eksternal/user.csv", 'r')
data_user = [None for i in range (103)] #Jumlah maksimum isi array data_user adalah 103, indeks 0 adalah "header" csv, indeks 1 adalah bandung bondowoso, indeks 2 adalah roro jonggrang, sisanya ada maksimal 100 jin.

# Melakukan .split pada data user di file "user.csv"
i=0
for baris in user.readlines():
    data_user[i] = splitLuSendiri(baris,3)
    i+=1

username_arr = [None for i in range(102)] #"Header" csv tidak disimpan, maka jumlah maksimum isi array hanya 102
password_arr = [None for i in range(102)]
role_arr = [None for i in range(102)]

for i in range (1, lenSendiri(data_user,103)):            
    username_arr[i-1]=((data_user[i][0]))
    password_arr[i-1]=((data_user[i][1]))
    role_arr[i-1]=((data_user[i][2]))

# Menutup kembali file "user.csv"
user.close()

# LOADING data dari file "candi.csv" ke dalam Array of Array of String dengan nama variabel data_candi
candi = open("eksternal/candi.csv", 'r')
data_candi = [None for i in range (101)] #Jumlah maksimum candi adalah 100, sehingga jumlah maksimum isi array data_candi adalah 101

# Melakukan .split pada data user di file "candi.csv"
i=0
for baris in candi.readlines():
    data_candi[i] = splitLuSendiri(baris,5)
    i+=1

# Menutup kembali file "candi.csv"
candi.close()

# LOADING data dari file "bahan_bangunan.csv" ke dalam Array of Array of String dengan nama variabel data_bahan_bangunan
bahan_bangunan = open("eksternal/bahan_bangunan.csv", 'r')
data_bahan_bangunan = [None for i in range (4)] #Ada 3 jenis bahan bangunan, maka jumlah maksimum isi array data_bahan_bangunan adalah 4

# Melakukan .split pada data user di file "bahan_bangunan.csv"
i=0
for baris in bahan_bangunan.readlines():
    data_bahan_bangunan[i] = splitLuSendiri(baris,3)
    i+=1

# Menutup kembali file "bahan_bangunan.csv"
bahan_bangunan.close()

# untuk menambah data apabila panjang dari list data_bahan_bangunan kosong
if lenSendiri(data_bahan_bangunan,1) == 1 :
    data_bahan_bangunan=isibahanbangunan(data_bahan_bangunan)
