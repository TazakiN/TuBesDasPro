from main import role
# (F16) Mendefinisikan Fungsi Exit
def exit() :
    inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (inp != "y" and inp != "n" and inp != "Y" and inp != "N"):
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if inp == "n" or inp == "N" :
        pass
    else : 
      save()
