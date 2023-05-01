# (F04) Mendefinisikan Fungsi Hapus Jin
from load_data import *

def hapusjin(data_candi : list ,username_arr : str) -> tuple:
    tes = 0
    unamejin = input("Masukkan username jin : ")
    for i in range(102): # looping untuk mengecek apakah username terdapat di dalam array, jika ada maka valid = True
        if username_arr[i]==unamejin:
            valid=True
            index=i # index disini nanti akan digunakan ketika ingin menghapus jin karena kita ingin mencari jin yang akan dihapus terletak dimana
            break
    else : 
        valid=False
    if valid==False :
        print("\nTidak ada jin dengan username tersebut.")
    else : # jika valid = True
        if unamejin == "Bondowoso" or unamejin == "Roro" or unamejin == "%":
            print("\nAnda tidak dapat menghapus " + unamejin + " dari alam gaib.")
        else :
            hapus = input("Apakah anda yakin ingin menghapus jin dengan username " + unamejin + " (Y/N)? ")
            if hapus == "Y" : #  menghapus jin 
                username_arr[index] = "%" # maka username, pass,dan role dari jin tersebut akan dihapus dengan diubah menjadi "%"
                role_arr[index] = "%"
                password_arr[index] = "%"
                print("\nJin telah dihapus dari alam gaib.")
                for i in range(1,101):
                    if data_candi[i] != "%" and data_candi[i][1] == unamejin: # untuk ketika jin tersebut membangun candi dan kita ingin menhapus jin
                        data_candi[i]="%"  # maka data_candi diubah menjadi "%"
                        for j in range(i+1, 101):  # untuk menggantikan data yang sudah dihilangkan dengan data selanjutnya
                            if data_candi[j] != "%":
                                data_candi[j-1], data_candi[j] = data_candi[j],data_candi[j-1]
                            else :
                                data_candi[j], data_candi[j-1] = data_candi[j-1],data_candi[j]
                return data_candi
            else : # jika hapus != Y
                print("\nJin tidak dihapus dari alam gaib.") 
    return data_candi,username_arr
