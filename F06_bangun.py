# Import
import random

# (F06) Mendefinisikan Fungsi Bangun
def bangun(uname, data_bahan_bangunan, data_candi) -> None:
    # Mendatkan data banyaknya bahan bangunan dari Array of Array of String data_bahan_bangunan
    sum_pasir = int(data_bahan_bangunan[1][2])
    sum_batu = int(data_bahan_bangunan[2][2])
    sum_air = int(data_bahan_bangunan[3][2])

    # Men-generate angka random untuk menentukan bahan yang dibutuhkan untuk membuat candi.
    need_bahan = [random.randint(1,5) for i in range(3)]
    
    # Menggagalkan pembangunan candi jika bahan tidak mencukupi
    if need_bahan[0] > sum_pasir or need_bahan[1] > sum_batu or need_bahan[2] > sum_air:
        print("Bahan Bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    else:   # Saat bahan mencukupi kebutuhan untuk membuat satu candi
        # Mengurangi bahan yang dimiliki pada variabel sum sesuai kebutuhan bahan
        sum_pasir -= need_bahan[0]
        sum_batu -= need_bahan[1]
        sum_air -= need_bahan[2]

        # Merubah banyak bahan pada Array of Array of String data_bahan_bangunan
        data_bahan_bangunan[1][2] = str(sum_pasir)
        data_bahan_bangunan[2][2] = str(sum_batu)
        data_bahan_bangunan[3][2] = str(sum_air)

        # Membangun candi pada Array of Array of String data_candi
        for iter in range(101):
            if data_candi[iter] == None:
                data_candi[iter] = ["" for i in range(5)]
                data_candi[iter][0] = iter
                data_candi[iter][1] = uname
                data_candi[iter][2] = str(need_bahan[0])
                data_candi[iter][3] = str(need_bahan[1])
                data_candi[iter][4] = str(need_bahan[2])
                print("Candi berhasil dibangun.")
                print("Sisa candi yang perlu dibangun:", 100 - iter)
                break
            if iter == 100:
                print("Candi berhasil dibangun")
                print("Sisa candi yang perlu dibangun: 0")

