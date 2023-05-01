# util.py
# File ini digunakan untuk menyimpan semua fungsi/prosedur yang akan digunakan berulang kali dan atau
#   mendeklarasi dan mendefenisikan fungsi yang kita buat sendiri

# Membuat fungsi setara .split() sendiri
def splitLuSendiri(sebaris, x):
    # x adalah jumlah kolom di csv
    temp = ""
    hasil = ["%" for i in range (x)]
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
        if data[i]!='%':
            panjang += 1
    return panjang

# untuk mengisi data di bahan bangunan
def isibahanbangunan(array : list) -> list:
    array[1] =['Pasir','pasir asli sunagakure','0']
    array[2] =['Batu','batu biasa bukan batu akik','0']
    array[3] =['Air','air mata TPB','0']
    return array

# Untuk menentukan banyak kekurangan bahan pada file F08_batch fungsi batchbangun.
def kurangBerapa(tersedia, butuh) -> int:
    if tersedia >= butuh:
        return 0
    else:
        return butuh - tersedia
    
# untuk menghapus sebaris data pada matrix
def delete(data_candi,index):
    data_candi = [e for e in data_candi if e != data_candi[index]]

def cariindeksterakhir(arr,N):
#Fungsi ini untuk mencari indeks terakhir yang memiliki isi di sebuah array
    totalisi=lenSendiri(arr,N)
    isi=0
    for i in range(N):
        if arr[i]!="%":
            isi+=1
        if isi==totalisi:
            break
    return i
