# (F07) Mendefinisikan Fungsi Kumpul
from random import randint
from util import *
from load_data import *

def kumpul():
    p = randint(0,5)
    b = randint(0,5)
    a = randint(0,5)
    data_bahan_bangunan[1][2] = int(data_bahan_bangunan[1][2])    
    data_bahan_bangunan[2][2] = int(data_bahan_bangunan[2][2])
    data_bahan_bangunan[3][2] = int(data_bahan_bangunan[3][2])
    data_bahan_bangunan[1][2] += p
    data_bahan_bangunan[2][2] += b
    data_bahan_bangunan[3][2] += a
    print(f"Jin menemukan {p} pasir, {b} batu, dan {a} air.")
    return data_bahan_bangunan
