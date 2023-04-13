from load_data import *

# (F01) Mendefinisikan Fungsi Login 
def login():
    # Menerima masukan usernam dan password dari pengguna ke variabel uname dan passs 
    uname = input("Username: ")
    passs = input("Password: ")
    # Melakukan pengecekan apakah masukan pengguna terdaftar pada "user.csv" atau tidakl
    for i in range (lenSendiri(username_arr,102)):
        if uname == username_arr[i]:
            if passs == password_arr[i]:
                print()
                print("Selamat datang, "+ str(uname)+"!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return role_arr[i]
            else:   # jika password yang dimasukkan salah
                print("Password salah!")
                return ""
    # jika username tidak terdapat pada "user.csv"
    print("Username tidak terdaftar!")
    return ""
