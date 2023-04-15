# main.py
# Menjadi file utama untuk menjalankan program

# import
from load_data import *     #setelah import load_data.py, kita punya variabel data_user, data_candi, dan data_bahan_bangunan
from util import *
from commands import *

# ALGORITMA UTAMA
# Mendeklarasikan variabel role yang menentukan fungsi yang dapat diakses
role = ""
uname = ""
# Melakukan looping untuk terus meminta prompt
while True:
    prompt = input(">>> ")
    run(prompt)
