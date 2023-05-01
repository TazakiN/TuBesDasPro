# (F11) Mendefinisikan Fungsi Hancurkan Candi
def hancurkancandi(data_candi):
    id = int(input("Masukkan ID candi: "))

    if 0 < id < lenSendiri(data_candi):
        verif = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
        if verif == 'Y' or verif == 'y':
            delete (data_candi,id)
            print("\nCandi telah berhasil dihancurkan.")
        else:
            print("\nCandi batal dihancurkan.")
    else :
        print("\nTidak ada candi dengan ID tersebut.")
