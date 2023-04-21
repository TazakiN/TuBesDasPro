# F12 - Ayam Berkokok
# Akses : Roro Jongrang

def ayamberkokok():
    if lenSendiri(data_candi) == 1 and data_candi[0][0] == 0:
        candiCount = 0
    else:
        candiCount = lenSendiri(data_candi)-1

    print("Kukuruyuk.. Kukuruyuk..\n")
    
    print(f"Jumlah Candi: {candiCount}\n")
    if lenSendiri(data_candi) < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
        # exit()
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        # exit()
