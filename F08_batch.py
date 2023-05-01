# (F08) Mendefinisikan Fungsi Batch Kumpul dan Batch Bangun
# import
from load_data import *
from random import randint
from util import kurangBerapa

# Mendefinisikan Fungsi Batch Kumpul
def batchkumpul(role_arr,data_bahan_bangunan):
    # Menghitung berapa banyak jin_pengumpul yang ada.
    banyak_pengumpul = 0
    for index_jin in range(102):
        if role_arr[index_jin] == "jin_pengumpul":
            banyak_pengumpul += 1

    if banyak_pengumpul == 0:   # Jika tidak terdapat jin pengumpul.
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:   # Jika terdapat jin pengumpul (setidaknya ada 1).
        # Mendeklarasikan variabel total masing-masing bahan untuk menyimpan total bahan yang terkumpul.
        total_pasir = 0
        total_batu = 0
        total_air = 0

        # Melakukan looping untuk setiap jin pengumpul mengumpulkan bahan.
        for jin in range(banyak_pengumpul):
            # Mendapatkan jumlah pasir, batu, dan air yang terkumpul oleh satu jin, kemudian menambahkan total bahan yang dari terkumpul ke variabel totalnya.
            total_pasir += randint(0,5)
            total_batu += randint(0,5)
            total_air += randint(0,5)

        # Merubah data pada Array data_bahan_bangunan sesuai total bahan yang terkumpul.
        data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2]) + total_pasir)  
        data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2]) + total_batu)
        data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2]) + total_air)

        # Mengakhiri fungsi dengan menampilkan output ke terminal.
        print(f"Mengerahkan {banyak_pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
    return data_bahan_bangunan

def batchbangun(username_arr, role_arr,data_bahan_bangunan,data_candi):
 
    # Menghitung banyak jin pembangun yang ada.
    banyak_pembangun = 0
    for index_jin in range(102):
        if role_arr[index_jin] == "jin_pembangun":
            banyak_pembangun += 1
    
    if banyak_pembangun == 0:   # Jika tidak terdapat Jin Pembangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:   # Jika terdapat Jin Pembangun (setidaknya 1)
        # Mendapatkan data banyaknya bahan bangunan dari Array of Array of String data_bahan_bangunan.
        sum_pasir = int(data_bahan_bangunan[1][2])
        sum_batu = int(data_bahan_bangunan[2][2])
        sum_air = int(data_bahan_bangunan[3][2])

        # Mendeklarasikan variabel total kebutuhan untuk masing-masing bahan.
        total_butuh_pasir, total_butuh_batu, total_butuh_air = 0, 0, 0

        all_need_bahan = ["y" for i in range(banyak_pembangun)]
        # Melakukan looping untuk setiap jin pembangun
        for index_jin in range(102):
            if role_arr[index_jin] == "jin_pembangun":
                # Men-generate angka random untuk menentukan bahan yang dibutuhkan untuk membuat candi.
                need_bahan = [randint(1,5) for i in range(3)]
                
                # Mengurangi bahan yang dimiliki pada variabel sum sesuai kebutuhan bahan
                total_butuh_pasir += need_bahan[0]
                total_butuh_batu += need_bahan[1]
                total_butuh_air += need_bahan[2]

                # Menambah data pada all_need_bahan
                for p in range(banyak_pembangun):
                    if all_need_bahan[p] == "y":
                        all_need_bahan[p] = [0 for i in range(3)]
                        for j in range(3):
                            all_need_bahan[p][j] = need_bahan[j]
        
        # Menampilkan berapa banyak Jin Pembangun yang bekerja dan total bahan yang dibutuhkan jika pembangunan dilakukan.
        print(f"Mengerahkan {banyak_pembangun} jin untuk membangun candi dengan total bahan {total_butuh_pasir} pasir, {total_butuh_batu} batu, dan {total_butuh_air} air.")

        if sum_pasir >= total_butuh_pasir and sum_batu >= total_butuh_batu and sum_air >= total_butuh_air: # Jika bahan yang tersedia mencukupi kebutuhan batchbangun.
            print(f"Jin berhasil membangun total {banyak_pembangun}")
            
            # Merubah banyak bahan pada Array of Array of String data_bahan_bangunan
            data_bahan_bangunan[1][2] = str(sum_pasir - total_butuh_pasir)
            data_bahan_bangunan[2][2] = str(sum_batu - total_butuh_batu)
            data_bahan_bangunan[3][2] = str(sum_air - total_butuh_air)
            
            # Merubah array data candi 
            for l in range(banyak_pembangun):
                # mencari nama dari jin pembangun saat ini
                for f in range(102):
                    if role_arr[f] == "jin_pembangun":
                        uname = username_arr[f]

                        # Membangun candi pada Array of Array of String data_candi
                        for iter in range(101):
                            if data_candi[iter] == "%":
                                # Merubah array data_candi pada index [iter]
                                data_candi[iter] = ["" for i in range(5)]
                                data_candi[iter][0] = str(iter)
                                data_candi[iter][1] = uname
                                data_candi[iter][2] = str(all_need_bahan[l][0])
                                data_candi[iter][3] = str(all_need_bahan[l][1])
                                data_candi[iter][4] = str(all_need_bahan[l][2])
                                break
                            if iter == 100: # Ketika array data_candi sudah penuh (berisi 100 candi)
                                # tidak melakukan perubahan apapun pada array data_candi
                                break
                        break

        else:   # Jika bahan yang tersedia tidak mencukupi untuk melakukan batch bangun
            print(f"Bangun gagal. Kurang {kurangBerapa(sum_pasir, total_butuh_pasir)} pasir, {kurangBerapa(sum_batu, total_butuh_batu)} batu, {kurangBerapa(sum_air, total_butuh_air)} air.")
    return username_arr, role_arr,data_bahan_bangunan,data_candi
