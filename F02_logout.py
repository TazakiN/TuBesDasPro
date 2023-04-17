# (F02) Mendefinisikan Fungsi Save
def logout(role) :
    if role != "" :
        role = ""
    else :
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return role

