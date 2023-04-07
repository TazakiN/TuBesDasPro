# main.py
# Menjadi file utama untuk menjalankan program

# import
from load_data import *     #setelah import load_data.py, kita punya variabel data_user, data_candi, dan data_bahan_bangunan
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
                print()
                print("Selamat datang, "+ str(uname)+"!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return satu_user[2]
            else:   # jika password yang dimasukkan salah
                print("Password salah!")
                return ""
    # jika username tidak terdapat pada "user.csv"
    print("Username tidak terdaftar!")
    return ""

# Mendefinisikan Fungsi Save
def save():
    pass

# Mendefinisikan Fungsi Help
def help():
    if role == "":
        print("""=========== HELP ===========
1. login
    Untuk masuk menggunakan akun
2. save
    Untuk menyimpan data permainan ke dalam sebuah folder
3. load
    Untuk memuat file eksternal ke dalam permainan
""")
    elif role == "bandung_bondowoso":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun Bandung Bondowoso
2. summonjin
    Untuk memanggil jin
3. hapusjin
    Untuk menghapus jin tertentu dan juga menghapus candi yang telah dibuat oleh jin tersebut
4. ubahjin
    Untuk mengubah jin tertentu menjadi jin pembangun atau jin pengumpul
5. batchkumpul
    Untuk memerintahkan semua jin pengumpul untuk mengumpulkan bahan-bahan
6. batchbangun
    Untuk memerintahkan semua jin pembangun untuk membangun candi
7. laporanjin
    Untuk menampilkan laporan mengenai kinerja jin
8. laporancandi
    Untuk menampilkan laporan mengenai progress pembangunan candi
9. save
    Untuk menyimpan data permainan ke dalam sebuah folder
10. load
    Untuk memuat file eksternal ke dalam permainan
11. exit
    Untuk keluar dari permainan
""")
    elif role == "roro_jonggrang":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
    Untuk menghancurkan candi yang tersedia
3. ayamberkokok
    Untuk menyelesaikan permainan dengan memalsukan pagi hari
4. save
    Untuk menyimpan data permainan ke dalam sebuah folder
5. load
    Untuk memuat file eksternal ke dalam permainan
6. exit
    Untuk keluar dari permainan
""")
    elif role == "jin_pengumpul":
        print("""=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi
3. save
    Untuk menyimpan data permainan ke dalam sebuah folder
4. load
    Untuk memuat file eksternal ke dalam permainan
5. exit
    Untuk keluar dari permainan
""")
    elif role == "jin_pembangun":
        print("""=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun sebuah candi
3. save
    Untuk menyimpan data permainan ke dalam sebuah folder
4. load
    Untuk memuat file eksternal ke dalam permainan
5. exit
    Untuk keluar dari permainan
""")

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
            if role == "":
                role = login() 
            else:
                print("Anda harus logout telebih dahulu!")
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
            save()

        case "help":
            help()

        case "exit":
            pass

        case _:
            print("Command yang dimasukkan tidak valid, ketik help untuk list command yang mungkin")
            continue