from F14_save import save
from load_data import *
# (F16) Mendefinisikan Fungsi Exit
def exit() :
    inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (inp != "y" and inp != "n" and inp != "Y" and inp != "N"):
        print("Input salah!")
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if inp == "y" or inp == "Y" :
        save(username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan)