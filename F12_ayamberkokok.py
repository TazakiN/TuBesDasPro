# (F12) Mendefinisikan Fungsi Ayam Berkokok
from util import *
from load_data import *
import sys
# F12 - Ayam Berkokok
# Akses : Roro Jongrang

def ayamberkokok(data_candi):
    print("Kukuruyuk.. Kukuruyuk..\n")
    count = 0   # inisialisasi count 
    for i in range(1,101):
        if data_candi[i] != "%" : 
            count += 1    # menghitung jumlah candi yang sudah dibangun
        else : pass 
    print(f"Jumlah Candi: {count}\n") 
    for i in range(1,101) :
        if data_candi[i] != "%" :
            if count == 100 : # jika jumlah candi 100 maka Bandung bondowoso memenangkan permainan
                print("Yah, Bandung Bondowoso memenangkan permainan!")
                sys.exit(1)
            else :
                print("Selamat, Roro Jonggrang memenangkan permainan!\n")
                print("*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.") # jika jumlah candi < 100 maka roro jonggrang memenangkan permainan
                sys.exit(1)
    return data_candi
