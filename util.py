# util.py
# File ini digunakan untuk menyimpan semua fungsi/prosedur yang akan digunakan berulang kali dan atau
#   mendeklarasi dan mendefenisikan fungsi yang kita buat sendiri

# Membuat fungsi setara .split() sendiri
def splitLuSendiri(sebaris, x):
    # x adalah jumlah kolom di csv
    temp = ""
    hasil = [None for i in range (x)]
    j=0
    for i in range(len(sebaris)):
        if sebaris[i]==';' or i==len(sebaris)-1:
            if i==len(sebaris)-1 and sebaris[i]!='\n':
                temp += sebaris[i]
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
        if data[i]!=None:
            panjang += 1
    return panjang

# untuk mengisi data di bahan bangunan
def isibahanbangunan(array):
    array[1] =['Pasir','lorem ipsum','0']
    array[2] =['Air','lorem ipsum','0']
    array[3] =['Batu','lorem ipsum','0']
    return array

# untuk mengisi data candi 
def isidatacandi(array):
    array[1] = [0,0,0,0,0]
    return array

# Untuk menentukan banyak kekurangan bahan pada file F08_batch fungsi batchbangun.
def kurangBerapa(tersedia, butuh) -> int:
    if tersedia >= butuh:
        return 0
    else:
        return butuh - tersedia
