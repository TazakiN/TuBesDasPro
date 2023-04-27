# (F02) Mendefinisikan Fungsi Save

def logout(role : str) -> str :
    # jika sudah login artinya role sudah terisi, maka agar bisa logout role akan dikosongin kembali
    if role != "" :
        role = ""
        print("Anda telah keluar dari akun...\nSilakan login kembali jika perlu.")
    else : # jika role sudah kosong, maka tidak bisa logout lagi sampai role sudah terisi kembali
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return role


