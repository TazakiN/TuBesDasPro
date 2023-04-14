# (F04) Mendefinisikan Fungsi Hapus Jin
def hapusjin():
    unamejin = input("Masukkan username: ")
    for i in range(102):
        if username_arr[i]==unamejin:
            valid=True
            index=i
            break
    else: valid=False
    if valid==False :
        print("Tidak ada jin dengan username tersebut.")
    else :
        username_arr[index]=None
        role_arr[index]=None
        password_arr[index]=None
        print(f"Jin dengan username {unamejin} telah  dihapus")
