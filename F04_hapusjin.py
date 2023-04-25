# (F04) Mendefinisikan Fungsi Hapus Jin
from load_data import *

def hapusjin():
    unamejin = input("Masukkan username jin : ")
    for i in range(102):
        if username_arr[i] == unamejin:
            valid = True
            index = i
            break
    else : 
        valid = False
    if valid == False :
        print("\nTidak ada jin dengan username tersebut.")
    else :
        hapus = input(f"Apakah anda yakin ingin menghapus jin dengan username {unamejin} (Y/N)? ")
        if hapus == "Y" :
            username_arr[index] = None
            role_arr[index] = None
            password_arr[index] = None
            print(f"\nJin telah dihapus dari alam gaib.")
            for i in range (1,101):
                if data_candi[i] != None and data_candi[i][1] == unamejin:
                    data_candi[i] = None
        else : print("\nJin tidak dihapus dari alam gaib.")
