# F12 - Ayam Berkokok
# Akses : Roro Jongrang

def ayamberkokok():
    print("Kukuruyuk.. Kukuruyuk..\n")
    count = 0   # inisialisasi count 
    for i in range(1,101):
        if data_candi[i] != "%" : 
            count += 1    # menghitung jumlah candi yang sudah dibangun
        else : pass 
    print(f"Jumlah Candi: {count}\n") 
    tes = 0
    for i in range(1,101) :
        if data_candi[i] != "%" :
            if count == 100 : # jika jumlah candi 100 maka Bandung bondowoso memenangkan permainan
                tes = 0
            else :
                tes = 1 # jika jumlah candi < 100 maka roro jonggrang memenangkan permainan
        else : 
            pass
    if tes == 0 :
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else :
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
