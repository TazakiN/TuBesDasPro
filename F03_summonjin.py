# (F03) Mendefinisikan Fungsi Summon Jin
from util import *
from load_data import *

def summonjin(username_arr : str, password_arr: str, role_arr: str) -> tuple : 
    # jika array dari username sudah mencapai 102(karena termasuk Bondowoso dan roro), maka fungsi tidak bisa dijalankan lagi
    if lenSendiri(username_arr,102) == 102 : 
        print("Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else : # jika jumlah jin belum mencapai 100
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        n = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
        while n != 1 and n != 2 : # akan dilakukan looping terus menerus sampai inputnya benar yaitu 1 atau 2
            if n < 1 or n > 2 : # jika bukan memilih jin Pengumpul maupun Pembangun
                print(f"\nTidak ada jenis jin bernomor “{n}”!")
            n = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
        if 1 <= n <= 2 :
            if n == 1 : # jika memilih 1 maka akan memilih jin pengumpul
                jenis_jin = "jin_pengumpul"
                x = "Pengumpul"
            else: # memilih jin pembangun
                jenis_jin = "jin_pembangun"
                x = "Pembangun"
            print(f"\nMemilih jin \"{x}\".")
            unamejin = str(input("\nMasukkan username jin: "))
            valid = False 
            for i in range(102) : # looping seluruh sebanyak 102 sepanjang array username untuk mengecek apakah terdapat username yang sama dalam satu array
                if unamejin == username_arr[i] : # jika username sudah terdapat dalam array maka valid akan menjadi True
                    valid = True
                    break
            while valid : # akan looping terus menerus jika valid = True yang artinya username terdapat di username_arr
                print(f"Username \"{unamejin}\" sudah diambil!")
                unamejin = str(input("\nMasukkan username jin: "))
                for i in range(102) :
                    if unamejin == username_arr[i] :
                        valid = True
                        break
                else:valid=False
            passjin = str(input("Masukkan password jin: "))
            # jika valid = False maka tidak akan menjalankan while valid dan akan langsung ke code di bawah ini
            if valid == False :
                x = len(passjin) 
                while not (5 <= x <= 25): # akan dilakukan looping terus menerus jika password yang dimasukkan tidak diantara 5 sampai 25 karakter
                    print("\npassword panjangnya harus 5-25 karakter!")
                    passjin = str(input("\nMasukkan password jin: "))
                    x = len(passjin)
            for i in range (102):
                if username_arr[i]==None: # jika semua sudah valid, maka dilakukan ini agar username, password dan role akan disimpan ke dalam array 
                    username_arr[i]=unamejin
                    password_arr[i]=passjin
                    role_arr[i]=jenis_jin
                    break
            print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
            print(f"\nJin {unamejin} berhasil dipanggil!") 
    return username_arr,password_arr,role_arr
