# (F10) Mendefinisikan Fungsi Laporan Candi
def laporancandi(data_candi):
    totalcandi = 0
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    id_termurah = 0
    id_termahal = 0
    termahal = -9999999 # inisialisasi dengan angka yang sangat kecil untuk mencari nilai maksimum 
    termurah = 9999999  # inisialisasi dengan angka yang sangat besar untuk mencari nilai minimum
    for i in range(1,101) :
        if data_candi[i] != "%" : # jika data_candi sudah terisi
            totalcandi += 1
            totalpasir += int(data_candi[i][2])
            totalbatu += int(data_candi[i][3])
            totalair += int(data_candi[i][4])
            harga = int(data_candi[i][2])*10000 + int(data_candi[i][3])*15000 + int(data_candi[i][4])*7500
            if harga > termahal: # untuk mencari nilai maks
                termahal = harga
                id_termahal = int(data_candi[i][0])
            if harga < termurah : # untuk mencari nilai min
                termurah=harga
                id_termurah = int(data_candi[i][0])
        else : 
            pass
    formattermahal = "{:,.0f}".format(termahal).replace(",", ".") # format agar sesuai dengan testcase
    formattermurah = "{:,.0f}".format(termurah).replace(",", ".")
    print("\n> Total Candi: ",totalcandi)
    print("> Total Pasir yang digunakan: ",totalpasir)
    print("> Total Batu yang digunakan: ",totalbatu)
    print("> Total Air yang digunakan: ",totalair)
    if totalcandi != 0 : # ketika candi tidak kosong
        print("> ID Candi Termahal: " +str(id_termahal)+ " (Rp " +str(formattermahal)+")")
        print("> ID Candi Termurah: " +str(id_termurah)+ " (Rp " +str(formattermurah)+")")
    else : # jika candi kosong
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")
