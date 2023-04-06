# load_data.py
# File ini digunakan untuk meload semua data saat awal memulai program

from util import *


# LOADING data dari file "user.csv" ke dalam Array of Array of String dengan nama variabel data_user
user = open("eksternal/user.csv", 'r')
data_user = []

# Melakukan .split pada data user di file "user.csv"
for baris in user.readlines():
    data_user += [splitLuSendiri(baris)]

# Menutup kembali file "user.csv"
user.close()


# LOADING data dari file "candi.csv" ke dalam Array of Array of String dengan nama variabel data_candi
candi = open("eksternal/candi.csv", 'r')
data_candi = []

# Melakukan .split pada data user di file "candi.csv"
for baris in candi.readlines():
    data_candi += [splitLuSendiri(baris)]

# Menutup kembali file "candi.csv"
candi.close()



# LOADING data dari file "bahan_bangunan.csv" ke dalam Array of Array of String dengan nama variabel data_bahan_bangunan
bahan_bangunan = open("eksternal/user.csv", 'r')
data_bahan_bangunan = []

# Melakukan .split pada data user di file "bahan_bangunan.csv"
for baris in bahan_bangunan.readlines():
    data_bahan_bangunan += [splitLuSendiri(baris)]

# Menutup kembali file "bahan_bangunan.csv"
bahan_bangunan.close()
