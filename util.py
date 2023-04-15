# util.py
# File ini digunakan untuk menyimpan semua fungsi/prosedur yang akan digunakan berulang kali dan atau
#   mendeklarasi dan mendefenisikan fungsi yang kita buat sendiri

# Membuat fungsi setara .split() sendiri
def splitLuSendiri(sebaris, x):
    # x adalah jumlah kolom di csv
    temp = ""
    hasil = [None for i in range (x)]
    j=0
    for i in range(len(sebaris)): #karena len string diperbolehkan
        if sebaris[i]==';' or i==len(sebaris)-1:
            hasil[j] = temp
            j+=1
            temp = ""
        else: temp += sebaris[i]
    return hasil

# Membuat fungsi setara len() untuk menghitung jumlah indeks yang berisi dari sebuah array yang panjangnya diketahui
def lenSendiri(data, N): 
    # N adalah panjang dari array
    panjang = 0
    for i in range(N):
        if data[i]==None:
            break
        else:
            panjang += 1
    return panjang
