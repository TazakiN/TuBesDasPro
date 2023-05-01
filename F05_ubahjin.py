# (F05) Mendefinisikan Fungsi Ubah Jin 
from load_data import *


def ubahjin(username_arr : str, role_arr : str) -> tuple :
    unamejin = input("Masukkan username jin : ")
    valid = True
    for i in range(102): # akan dilakukan looping untuk mencari apakah username terdapat di dalam array atau tidak
        if username_arr[i] == unamejin: # jika terdapat maka valid = True
            valid = True
            indeks = i  # indeks digunakan untuk mencari lokasi dari jin dalam array
            break
    else: 
        valid = False
    if valid == False :
        print("\nTidak ada jin dengan username tersebut.")
    else : # valid == True
        # jika role dari jin tersebut adalah bandung_bondowoso atau roro_jonggrang maka jin tersebut bukan pembangun maupun pengumpul
        if role_arr[indeks] == "bandung_bondowoso" or role_arr[indeks] == "roro_jonggrang" or role_arr[indeks]== "%": 
            print("\nUsername \"" + unamejin + "\" bukan jin pengumpul maupun jin pembangun.")
        elif role_arr[indeks] == "jin_pengumpul" : 
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if ubah == "Y" :
                role_arr[indeks] = "jin_pembangun" # role diubah menjadi jin_pembangun karena role jin awalnya adalah jin_pengumpul
                print("\nJin telah berhasil diubah.")
            elif ubah == "N" : 
                print("\nJin ini tidak diubah.")
            else : # input != "N" or input != "Y"
                print("\nInput tidak sesuai format!")
        else : # role_arr[indeks] == jin_pembangun
            ubah = (input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
            if ubah == "Y"  :
                role_arr[indeks] = "jin_pengumpul" # role diubah menjadi jin_pengumpul karena role jin awalnya adalah jin_pengumpul
                print("\nJin telah berhasil diubah.") 
            elif ubah == "N" : 
                print("\nJin ini tidak diubah.")
            else : # input != "N" or input != "Y"
                print("\nInput tidak sesuai format!")
    return username_arr,role_arr
    

