# (F05) Mendefinisikan Fungsi Ubah Jin 
def ubahjin():
    global username_arr, password_arr, role_arr
    unamejin = input("Masukkan username jin : ")
    valid = True
    for i in range(102):
        if username_arr[i] == unamejin:
            valid = True
            indeks = i
            break
    else: valid = False
    if valid == False :
        print("Tidak ada jin dengan username tersebut.")
    else :
        if role_arr[indeks] == "Pengumpul" :
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if ubah == "Y" or ubah == "y" :
                role_arr[indeks] = "Pembangun"
                print("\nJin telah berhasil diubah.")
            else : pass
        else :
            ubah = (input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
            if ubah == "Y" or ubah =="y" :
                role_arr[indeks] = "Pengumpul"
                print("\nJin telah berhasil diubah.")
            else : pass
