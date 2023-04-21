# (F13) Mendefinisikan Fungsi Load
from util import *
import argparse
import os.path

def load() -> tuple :
    # Fungsi ini digunakan untuk meload semua data saat awal memulai program
    parser=argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Nama folder letak file-file game.",nargs="?")
    args = parser.parse_args()
    if args.nama_folder == None:
        italic_text = "\x1B[3m" + "python main.py" + "\x1B[0m"
        print("\nTidak ada nama folder yang diberikan!")
        print(f"\nUsage: {italic_text} <nama_folder>")
        exit()
    elif not os.path.isdir(args.nama_folder):
        print(f"\nFolder \"{args.nama_folder}\" tidak ditemukan.")
        exit()
    else:
        print("\nLoading...")
        # LOADING data dari file "user.csv" ke dalam Array of Array of String dengan nama variabel data_user
        user = open(args.nama_folder+"/user.csv", 'r')
        data_user = [None for i in range (103)] #Jumlah maksimum isi array data_user adalah 103, indeks 0 adalah "header" csv, indeks 1 adalah bandung bondowoso, indeks 2 adalah roro jonggrang, sisanya ada maksimal 100 jin.
        i=0
        for baris in user.readlines():
            data_user[i] = splitLuSendiri(baris,3)
            i+=1
        # Memisahkan data username, password, dan role ke array masing-masing
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
        candi = open(args.nama_folder+"/candi.csv", 'r')
        data_candi = [None for i in range (101)] #Jumlah maksimum candi adalah 100, sehingga jumlah maksimum isi array data_candi adalah 101
        i=0
        for baris in candi.readlines():
            data_candi[i] = splitLuSendiri(baris,5)
            i+=1
        # Menutup kembali file "candi.csv"
        candi.close()

        # LOADING data dari file "bahan_bangunan.csv" ke dalam Array of Array of String dengan nama variabel data_bahan_bangunan
        bahan_bangunan = open(args.nama_folder+"/bahan_bangunan.csv", 'r')
        data_bahan_bangunan = [None for i in range (4)] #Ada 3 jenis bahan bangunan, maka jumlah maksimum isi array data_bahan_bangunan adalah 4
        i=0
        for baris in bahan_bangunan.readlines():
            data_bahan_bangunan[i] = splitLuSendiri(baris,3)
            i+=1
        # Menutup kembali file "bahan_bangunan.csv"
        bahan_bangunan.close()
        print("\nSelamat datang di program Manajerial Candi")
        print("Silakan masukkan username Anda")
        return username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan
