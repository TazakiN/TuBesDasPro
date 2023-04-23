from F01_login import *
from F02_logout import *
from F03_summonjin import *
from F04_hapusjin import *
from F05_ubahjin import *
from F06_bangun import *
from F07_kumpul import *
from F08_batch import *
from F09_laporanjin import *
from F10_laporancandi import *
from F11_hancurkancandi import *
from F12_ayamberkokok import *
from F14_save import *
from F15_help import *
from F16_exit import *

role = ""
uname = ""


def run(prompt) -> None:
    global role
    global uname

    if prompt == "login":  
        role,uname = login(uname, role) 
    elif prompt ==  "logout":
        role = logout(role)
    elif prompt == "summonjin":
        if role == "bandung_bondowoso":
            summonjin(username_arr, password_arr, role_arr)
        else:
            print("summonjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "hapusjin":
        if role == "bandung_bondowoso":
            hapusjin()
        else:
                print("hapusjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "ubahjin":
        if role == "bandung_bondowoso":
            ubahjin(username_arr, role_arr)
        else:
            print("ubahjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "bangun":
        if role == "jin_pembangun":
            bangun(uname, data_bahan_bangunan, data_candi)
        else:
            print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
    elif prompt == "kumpul":
        if role == "jin_pengumpul":
            kumpul()
        else:
            print("kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    elif prompt == "batchkumpul":
        if role == "bandung_bondowoso":
            batchkumpul(role_arr, data_bahan_bangunan)
        else:
            print("batchkumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "batchbangun":
        if role == "bandung_bondowoso":
            batchbangun(username_arr, role_arr, data_bahan_bangunan, data_candi)
        else:
            print("batchbangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "laporanjin":
        if role == "bandung_bondowoso":
            laporanjin()
        else:
            print("laporanjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt ==  "laporancandi":
        if role == "bandung_bondowoso":
            laporancandi()
        else:
            print("laporancandi hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif prompt == "hancurkancandi":
        if role == "roro_jonggrang":
            hancurkancandi()
        else:
            print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.")
    elif prompt == "ayamberkokok":
        if role == "roro_jonggrang":
            ayamberkokok()
        else:
            print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    elif prompt == "save":
        save()

    elif prompt == "help":
        help(role=role)

    elif prompt == "exit":
        exit()
    else :
        print("Command yang dimasukkan tidak valid, ketik help untuk list command yang mungkin")
