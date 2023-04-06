# main.py
# Menjadi file utama untuk menjalankan program

# import
from load_data import *
from util import *
from bandung_bondowoso import *
from roro_jonggrang import *
from jin_pembangun import *
from jin_pengumpul import *

# Mendefinisikan Fungsi Login
def login():
    # Menerima masukan usernam dan password dari pengguna ke variabel uname dan passs 
    uname = input("Username: ")
    passs = input("Password: ")
    # Melakukan pengecekan apakah masukan pengguna terdaftar pada "user.csv" atau tidak
    for satu_user in data_user:
        if uname == satu_user[0]:
            if passs == satu_user[1]:
                return satu_user[2]
            else:   # jika password yang dimasukkan salah
                print("Password salah!")
                return ""
    # jika username tidak terdapat pada "user.csv"
    print("Username tidak terdaftar!")
    return ""


# ALGORITMA UTAMA
# Mendeklarasikan variabel role yang menentukan fungsi yang dapat diakses
role = ""
# Melakukan looping untuk terus meminta prompt
while True:
    # Menerima masukan prompt dari pengguna
    prompt = input(">>> ")

    # Melakukan validasi akun dan kemudian melakukan tindakan sesuai prompt yang dimasukkan
    match prompt:
        case "login":
            role = login() 
            if role == "":
                continue
        case "logout":
            role = ""
            continue
        case "summonjin":
            if role == "bandung_bondowoso":
                summonjin()
            else:
                print("summonjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "hapusjin":
            if role == "bandung_bondowoso":
                hapusjin()
            else:
                print("hapusjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "ubahjin":
            if role == "bandung_bondowoso":
                ubahjin()
            else:
                print("ubahjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "bangun":
            if role == "jin_pembangun":
                bangun()
            else:
                print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
        case "kumpul":
            if role == "jin_pengumpul":
                kumpul()
            else:
                print("kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
        case "batchkumpul":
            if role == "bandung_bondowoso":
                batchkumpul()
            else:
                print("batchkumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "batchbangun":
            if role == "bandung_bondowoso":
                batchbangun()
            else:
                print("batchbangun hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "laporanjin":
            if role == "bandung_bondowoso":
                laporanjin()
            else:
                print("laporanjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "laporancandi":
            if role == "bandung_bondowoso":
                laporancandi()
            else:
                print("laporancandi hanya dapat diakses oleh akun Bandung Bondowoso.")
        case "hancurkancandi":
            if role == "roro_jonggrang":
                hancurkancandi()
            else:
                print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.")
        case "ayamberkokok":
            if role == "ayamberkokok":
                ayamberkokok()
            else:
                print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
        case "save":
            TODO()

        case "help":
            TODO()

        case "exit":
            exit()

        case _:
            print("Perintah yang dimasukkan tidak valid, ketik help untuk list perintah yang mungkin")
            continue