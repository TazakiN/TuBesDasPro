# util.py
# File ini digunakan untuk menyimpan semua fungsi/prosedur yang akan digunakan berulang kali dan atau
#   mendeklarasi dan mendefenisikan fungsi yang kita buat sendiri

# Membuat fungsi setara .split() sendiri
def splitLuSendiri(sebaris):
    temp = ""
    hasil = []
    for i in range(my_len(sebaris) - 1):
        if sebaris[i] != ';':
            temp += sebaris[i]
        else:
            hasil = hasil + [temp]
            temp = ""
    hasil = hasil + [temp]
    return hasil

def my_len(data):
    count = 0
    for el in data:
        count+= 1
    return count