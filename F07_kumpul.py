# (F07) Mendefinisikan Fungsi Kumpul
from random import randint
from load_data import *

def kumpul():
    global data_bahan_bangunan    
    # Mendapatkan jumlah pasir, batu, dan air yang terkumpul
    pasir_terkumpul = randint(0,5)
    batu_terkumpul = randint(0,5)
    air_terkumpul = randint(0,5)

    # Merubah data_bahan_bangunan sesuai bahan yang terkumpul
    data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2]) + pasir_terkumpul)  
    data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2]) + batu_terkumpul)
    data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2]) + air_terkumpul)

    print(f"Jin menemukan {pasir_terkumpul} pasir, {batu_terkumpul} batu, dan {air_terkumpul} air.")