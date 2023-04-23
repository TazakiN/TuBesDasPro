# (F05) Mendefinisikan Fungsi Ubah Jin 
from load_data import *

def ubahjin(username_arr, role_arr):
    unamejin = input("Masukkan username jin : ")
    valid = True
    for i in range(102):
        if username_arr[i] == unamejin:
            valid = True
            indeks = i
            break
    else: valid = False
    if valid == False :
        print("\nTidak ada jin dengan username tersebut.")
    else :
        if role_arr[indeks] == "bandung_bondowoso" or role_arr[indeks] == "roro_jonggrang" :
            print(f"\nUsername \"{unamejin}\" bukan jin pengumpul maupun jin pembangun.")
        elif role_arr[indeks] == "jin_pengumpul" :
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if ubah == "Y" :
                role_arr[indeks] = "jin_pembangun"
                print("\nJin telah berhasil diubah.")
            elif ubah == "N" : 
                print("\nJin ini tidak diubah.")
            else : print("Input tidak sesuai format!")
        else :
            ubah = (input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
            if ubah == "Y"  :
                role_arr[indeks] = "jin_pengumpul"
                print("\nJin telah berhasil diubah.")
            elif ubah == "N" : 
                print("\nJin ini tidak diubah.")
            else : print("\nInput tidak sesuai format!")
    return username_arr,role_arr
    

