nama = "elfin"
pw = "24"
percobaan = 0

while percobaan < 3:
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    if username == nama and password == pw:
        print("Berhasil")

        while True:
            print("Selamat Datang di Peminjaman Online !")
            print("<=========================================================================================================================================>")
            nama = input("Masukkan Nama Lengkap : ")
            nim = input("Masukkan NIM : ")
            total_pinjaman = int(input("Masukkan Total Pinjaman : "))
            lama_cicilan = int(input("Masukkan Lama Cicilan (1 - 3 Tahun): "))

            if lama_cicilan == 1 : 
                bunga_perbulan = (0.07 / 12) * total_pinjaman
                cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 12
            elif lama_cicilan == 2:
                bunga_perbulan = (0.13 / 12) * total_pinjaman
                cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 24
            elif lama_cicilan == 3:
                bunga_perbulan = (0.07 / 12) * total_pinjaman
                cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 36

            print(f"atas Nama {nama} dengan NIM {nim} akan melakukan pinjaman sebesar {total_pinjaman} dengan cicilannya sebesar {cicilan_bulanan:.0f}")
            print("<=========================================================================================================================================>")

            mengulang = int(input("Apakah Anda Ingin Mengulang? ketik '1' untuk mengulang dan ketik '2' untuk keluar: "))
            if mengulang == 1:
                pass
            elif mengulang == 2:
                print("Program dihentikan")
                break
        break
    else:
        percobaan += 1
        print("Username atau Password Salah, Silahkan coba lagi")
        if percobaan == 3:
           print("Sudah 3 kali percobaan, silahakn coba lagi nanti.")