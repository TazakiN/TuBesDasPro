# (F09) Mendefinisikan Fungsi Laporan Jin
from load_data import *
from util import *

def laporanjin ():
    total_jin = 0
    total_jin_pengumpul = 0
    total_jin_pembangun = 0
    jumlah_pasir = data_bahan_bangunan[1][2]
    jumlah_batu = data_bahan_bangunan[2][2]
    jumlah_air = data_bahan_bangunan[3][2]
    list_jin_pembangun = ["%" for i in range (lenSendiri(username_arr,102))]

    for i in range (lenSendiri(username_arr,102)):
        if role_arr[i] == "jin_pengumpul":
            total_jin_pengumpul += 1
            total_jin += 1
        if role_arr[i] == "jin_pembangun":
            total_jin_pembangun += 1
            total_jin += 1
            list_jin_pembangun[i] = username_arr[i]

    data_jin_pembangun = [["%",0] for i in range (total_jin_pembangun)]
    for i in range (lenSendiri(username_arr,102)):
        if list_jin_pembangun == "%":
            continue
        user_jin = list_jin_pembangun[i]
        rajin = 0
        for j in range (lenSendiri(data_candi,101)):
            if user_jin == data_candi[j][1]:
                rajin += 1
        
        for j in range (lenSendiri(data_jin_pembangun,total_jin_pembangun)):
            if data_jin_pembangun[j] == ["%", 0]:
                data_jin_pembangun[j][0] = user_jin
                data_jin_pembangun[j][1] = rajin
                break

    jin_terajin = data_jin_pembangun[0][0]
    jin_termalas = data_jin_pembangun[0][0]
    max_rajin = data_jin_pembangun[0][1]
    min_malas = data_jin_pembangun[0][1]
    
    for i in range (total_jin_pembangun):
        if data_jin_pembangun[i][1] > max_rajin:
            max_rajin = data_jin_pembangun[i][1]
            jin_terajin = data_jin_pembangun[i][0]
        if data_jin_pembangun[i][1] == max_rajin:
            if data_jin_pembangun[i][0]<jin_terajin:
                jin_terajin = data_jin_pembangun[i][0]
        if data_jin_pembangun[i][1] < min_malas:
            min_malas = data_jin_pembangun[i][1]
            jin_termalas = data_jin_pembangun[i][0]
        if data_jin_pembangun[i][1] == min_malas:
            if data_jin_pembangun[i][0]<jin_termalas:
                jin_termalas = data_jin_pembangun[i][0]

    if total_jin_pembangun == 0:
        jin_terajin = "-"
        jin_termalas = "-"
    
    print(f"> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_jin_pengumpul}")
    print(f"> Total Jin Pembangun: {total_jin_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {jumlah_pasir}")
    print(f"> Jumlah Air: {jumlah_air}")
    print(f"> Jumlah Batu: {jumlah_batu}")
