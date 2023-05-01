# (F15) Mendefinisikan Fungsi Help
# fungsi load tidak untuk dipanggil, tolong jangan ditambahkan lagi

def help(role):
    if role == "":
        print("""=========== HELP ===========
1. login
    Untuk masuk menggunakan akun
2. exit
    Untuk keluar dari program dan kembali ke terminal
""")
    elif role == "bandung_bondowoso":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun Bandung Bondowoso
2. summonjin
    Untuk memanggil jin
3. hapusjin
    Untuk menghapus jin tertentu dan juga menghapus candi yang telah dibuat oleh jin tersebut
4. ubahjin
    Untuk mengubah jin tertentu menjadi jin pembangun atau jin pengumpul
5. batchkumpul
    Untuk memerintahkan semua jin pengumpul untuk mengumpulkan bahan-bahan
6. batchbangun
    Untuk memerintahkan semua jin pembangun untuk membangun candi
7. laporanjin
    Untuk menampilkan laporan mengenai kinerja jin
8. laporancandi
    Untuk menampilkan laporan mengenai progress pembangunan candi
9. save
    Untuk menyimpan data permainan ke dalam sebuah folder
10. exit
    Untuk keluar dari program dan kembali ke terminal
""")

    elif role == "roro_jonggrang":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
    Untuk menghancurkan candi yang tersedia
3. ayamberkokok
    Untuk menyelesaikan permainan dengan memalsukan pagi hari
4. save
    Untuk menyimpan data permainan ke dalam sebuah folder
5. exit
    Untuk keluar dari program dan kembali ke terminal
""")
    elif role == "jin_pengumpul":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun yang digunakan sekarang
2. kumpul
    Untuk mengumpulkan resource candi
3. save
    Untuk menyimpan data permainan ke dalam sebuah folder
4. exit
    Untuk keluar dari program dan kembali ke terminal
""")
    elif role == "jin_pembangun":
        print("""=========== HELP ===========
1. logout
    Untuk keluar dari akun yang digunakan sekarang
2. bangun
    Untuk membangun sebuah candi
3. save
    Untuk menyimpan data permainan ke dalam sebuah folder
4. exit
    Untuk keluar dari program dan kembali ke terminal
""")
