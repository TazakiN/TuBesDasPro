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
from F13_load import *
from F14_save import *
from F15_help import *
from F16_exit import *

def run(prompt) -> None:
    match prompt:
        case "login":
            if role == "":
                role = login() 
            else:
                print("Anda harus logout telebih dahulu!")
        case "logout":
            role = ""
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
            save()

        case "help":
            help()

        case "exit":
            pass

        case _:
            print("Command yang dimasukkan tidak valid, ketik help untuk list command yang mungkin")