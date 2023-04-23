# (F03) Mendefinisikan Fungsi Summon Jin
from util import *
from load_data import *

def summonjin(username_arr, password_arr, role_arr):
    # global username_arr, password_arr, unamejin, jenis_jin, role_arr
    if lenSendiri(username_arr,102) == 102 :
        print("Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else :
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        n = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
        while n != 1 and n != 2 :
            if n < 1 or n > 2 :
                print(f"\nTidak ada jenis jin bernomor “{n}”!")
            n = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
        if 1 <= n <= 2 :
            if n == 1 :
                jenis_jin = "jin_pengumpul"
                x = "Pengumpul"
            else: 
                jenis_jin = "jin_pembangun"
                x = "Pembangun"
            print(f"\nMemilih jin \"{x}\".")
            unamejin = str(input("\nMasukkan username jin: "))
            valid = False
            for i in range(102) :
                if unamejin == username_arr[i] :
                    valid = True
                    break
            while valid :
                print(f"Username \"{unamejin}\" sudah diambil!")
                unamejin = str(input("\nMasukkan username jin: "))
                for i in range(102) :
                    if unamejin == username_arr[i] :
                        valid = True
                        break
                else:valid=False
            passjin = str(input("Masukkan password jin: "))
            if valid == False :
                x = len(passjin) 
                while not (5 <= x <= 25):
                    print("\npassword panjangnya harus 5-25 karakter!")
                    passjin = str(input("\nMasukkan password jin: "))
                    x = len(passjin)
            for i in range (102):
                if username_arr[i]==None:
                    username_arr[i]=unamejin
                    password_arr[i]=passjin
                    role_arr[i]=jenis_jin
                    break
            print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
            print(f"\nJin {unamejin} berhasil dipanggil!") 
    return username_arr,password_arr,role_arr
