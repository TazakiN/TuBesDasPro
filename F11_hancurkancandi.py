# (F11) Mendefinisikan Fungsi Hancurkan Candi
from util import *
from load_data import *

def hancurkancandi(data_candi):
    id = input("Masukkan ID candi: ") # input
    for i in range(1,101) :
        if data_candi[i] != "%" and data_candi[i][0] == id : # mengecek apakah data candi tidak kosong dan terdapat id yang akan dicari dalam data candi
            verif = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
            if verif == "Y" : 
                data_candi[i] = "%"   # data_candi dibuat jadi "%" atau dihilangkan
                print("\nCandi telah berhasil dihancurkan.")
                for j in range(i+1, 101):  # untuk menggantikan data yang sudah dihilangkan dengan data selanjutnya
                    if data_candi[j] != "%":
                        data_candi[j-1], data_candi[j] = data_candi[j],data_candi[j-1]
                    else :
                        print(len(data_candi))
                        data_candi[j], data_candi[j-1] = data_candi[j-1],data_candi[j]
                        return data_candi 
            else : # jika verif != Y
                print("\nCandi batal dihancurkan.")
                return data_candi
    print("\nTidak ada candi dengan tersebut.") # jika tidak terdapat id pada data candi
    return data_candi