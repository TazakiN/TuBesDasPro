from load_data import *
def login(uname, role):
    if role=="":
        # Menerima masukan usernam dan password dari pengguna ke variabel uname dan passs 
        uname = input("Username: ")
        passs = input("Password: ")
        # Melakukan pengecekan apakah masukan pengguna terdaftar pada "user.csv" atau tidak
        for i in range (lenSendiri(username_arr,102)):
            if uname == username_arr[i]:
                if passs == password_arr[i]:
                    print("\nSelamat datang, "+ str(uname)+"!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    return role_arr[i],uname
                else:   # jika password yang dimasukkan salah
                    print("\nPassword salah!")
                    return "",""
        # jika username tidak terdapat pada "user.csv"
        print("\nUsername tidak terdaftar!")
        return "",""
    else:
        print(f"Login gagal!\nAnda telah login dengan username {uname}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
        return  "",""
