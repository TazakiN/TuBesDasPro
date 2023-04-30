# (F10) Mendefinisikan Fungsi Laporan Candi
def laporancandi():
    total_candi = len(data_candi) - 1
    total_pasir = 0
    total_batu = 0
    total_air = 0
    i = 0

    for i in range (lenSendiri(data_candi)-1) :
        total_pasir += int(data_candi[i+1][2])
        total_batu += int(data_candi[i+1][3])
        total_air += int(data_candi[i+1][4])

    mahal = None
    murah = None
    for i in range(1, lenSendiri(data_candi)):
        harga = 10000 * int(data_candi[i][2]) + 15000 * int(data_candi[i][3]) + 7500 * int(data_candi[i][4])
        if mahal == None:
            mahal = (data_candi[i][0], harga) # (id, harga)
            murah = (data_candi[i][0], harga) # (id, harga)
        else:
            if harga > mahal[1]:
                mahal = (data_candi[i][0], harga)
            if harga < murah[1]:
                murah = (data_candi[i][0], harga)

    print(f"> Total Candi: {total_candi}")
    print(f"> Total Pasir yang digunakan: {total_pasir}")
    print(f"> Total Batu yang digunakan: {total_batu}")
    print(f"> Total Air yang digunakan: {total_air}")
    if murah == None:
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")
    else:
        print(f"ID Candi Termahal: {mahal[0]} (Rp {mahal[1]})")
        print(f"ID Candi Termurah: {murah[0]} (Rp {murah[1]})")
