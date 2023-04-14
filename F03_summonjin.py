# (F03) Mendefinisikan Fungsi Summon Jin
def summonjin():
    global username_arr, password_arr, unamejin, jenis_jin
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
                jenis_jin = "Pengumpul"
            else: jenis_jin = "Pembangun"
            print(f"\nMemilih jin \"{jenis_jin}\".")
            unamejin = str(input("\nMasukkan username jin: "))
            uname_exists = unamejin in username_arr
            while uname_exists:
                print(f"Username \"{unamejin}\" sudah diambil!")
                unamejin = str(input("\nMasukkan username jin: "))
                uname_exists = unamejin in username_arr
            passjin = str(input("Masukkan password jin: "))
            x = len(passjin) 
            while not (5 <= x <= 25):
                print("\npassword panjangnya harus 5-25 karakter!")
                passjin = str(input("\nMasukkan password jin: "))
                x = len(passjin)
            username_arr = appendSendiri(username_arr,unamejin)
            password_arr = appendSendiri(password_arr,passjin)
            print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
            print(f"\nJin {unamejin} berhasil dipanggil!") 
