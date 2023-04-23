from F14_save import save
# (F16) Mendefinisikan Fungsi Exit
def exit() :
    inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (inp != "y" and inp != "n" and inp != "Y" and inp != "N"):
        print("Input salah!")
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if inp == "y" or inp == "Y" :
        save()