# main.py
# Menjadi file utama untuk menjalankan program

# import
from F13_load import load 
from commands import run

# ALGORITMA UTAMA
username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan=load()
# Mendeklarasikan variabel role_arr yang menentukan fungsi yang dapat diakses
# Melakukan looping untuk terus meminta prompt
if username_arr != None and password_arr != None and role_arr != None and data_candi != None and data_bahan_bangunan != None : 
    while True:
        prompt = input(">>> ")
        run(prompt)
