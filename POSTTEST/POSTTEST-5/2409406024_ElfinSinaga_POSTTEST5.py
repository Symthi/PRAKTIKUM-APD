pengguna = []
pajak_motor = [
    [1, 'Motor Satria', 250000, 'KT 1234 LK', 'Fajar'],
    [2, 'Motor Honda', 300000, 'KT 2374 AS', 'Ahnaf'],
    [3, 'Motor Scoopy', 500000, 'KT 3452 SD', 'Elfin']
]

while True:
    print("\n" + "="*40)
    print("    PROGRAM PEMBAYARAN PAJAK BERMOTOR  ")
    print("="*40)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("="*40)
    pilihan = input("Pilih opsi: ")

    if pilihan == '1':
        print("\n" + "-"*40)
        print("             LOGIN PENGGUNA         ")
        print("-"*40)
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        user = None
        for u in pengguna:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user:
            print(f"\nSelamat datang, {user[1]}!")

            if user[3] == 'admin':
                while True:
                    print("\n" + "="*40)
                    print("               MENU ADMIN         ")
                    print("="*40)
                    print("1. Tambah Jenis Motor")
                    print("2. Lihat Daftar Pajak Motor")
                    print("3. Edit Pajak Motor")
                    print("4. Hapus Jenis Motor")
                    print("5. Logout")
                    print("="*40)
                    pilihan_admin = input("Pilih opsi : ")

                    if pilihan_admin == '1':
                        print("\n" + "-"*40)
                        print("           TAMBAH JENIS MOTOR      ")
                        print("-"*40)
                        jenis_motor_baru = input("Masukkan jenis Motor : ")
                        biaya_baru = int(input("Masukkan biaya Pajak : "))
                        plat_nomor_baru = input("Masukkan Plat Nomor : ")
                        nama_pemilik_baru = input("Masukkan Nama Pemilik Motor : ")

                        pajak_motor.append([len(pajak_motor) + 1, jenis_motor_baru, biaya_baru, plat_nomor_baru, nama_pemilik_baru])
                        print("Berhasil menambahkan !")

                    elif pilihan_admin == '2':
                        print("\n" + "-"*40)
                        print("            DAFTAR PAJAK MOTOR      ")
                        print("-"*40)
                        for motor in pajak_motor:
                            print(f"ID : {motor[0]} | {motor[1]} | Pajak : {motor[2]} | Plat : {motor[3]} | Pemilik : {motor[4]}")
                        print("-"*40)

                    elif pilihan_admin == '3':
                        print("\n" + "-"*40)
                        print("            EDIT PAJAK MOTOR       ")
                        print("-"*40)
                        id_edit = int(input("Masukkan ID motor yang akan diedit : "))
                        for motor in pajak_motor:
                            if motor[0] == id_edit:
                                motor[2] = int(input(f"Masukkan biaya baru (sebelumnya : {motor[2]}): "))
                                print("Berhasil di Update !")
                                break
                        else:
                            print("Jenis motor tidak ditemukan!")

                    elif pilihan_admin == '4':
                        print("\n" + "-"*40)
                        print("            HAPUS JENIS MOTOR      ")
                        print("-"*40)
                        id_hapus = int(input("Masukkan ID motor yang akan dihapus : "))
                        for motor in pajak_motor:
                            if motor[0] == id_hapus:
                                pajak_motor.remove(motor)
                                print("Jenis motor berhasil dihapus!")
                                break
                        else:
                            print("kadada pang jenis motornya !")

                    elif pilihan_admin == '5':
                        print("Logout berhasil!")
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                while True:
                    print("\n" + "="*40)
                    print("               MENU PENGGUNA        ")
                    print("="*40)
                    print("1. Lihat Daftar Pajak Motor")
                    print("2. Bayar Pajak Motor")
                    print("3. Logout")
                    print("="*40)
                    pilihan_pengguna = input("Pilih opsi: ")

                    if pilihan_pengguna == '1':
                        print("\n" + "-"*40)
                        print("            DAFTAR PAJAK MOTOR      ")
                        print("-"*40)
                        for motor in pajak_motor:
                            print(f"ID : {motor[0]} | {motor[1]} | Pajak : {motor[2]} | Plat : {motor[3]} | Pemilik : {motor[4]}")
                        print("-"*40)

                    elif pilihan_pengguna == '2':
                        print("\n" + "-"*40)
                        print("         PEMBAYARAN PAJAK MOTOR    ")
                        print("-"*40)
                        id_pajak = int(input("Masukkan ID motor yang ingin dibayar pajaknya : "))
                        for motor in pajak_motor:
                            if motor[0] == id_pajak:
                                print(f"Pajak {motor[1]} sebesar {motor[2]} telah dibayar !")
                                break
                        else:
                            print("kadada pang jenis motornya !")

                    elif pilihan_pengguna == '3':
                        print("Logout berhasil !")
                        break
                    else:
                        print("Pilihan tidak valid !")
        else:
            print("Username atau password salah!")

    elif pilihan == '2':
        print("\n" + "-"*40)
        print("           REGISTRASI PENGGUNA        ")
        print("-"*40)
        username_baru = input("Masukkan username baru : ")

        for user in pengguna:
            if user[1] == username_baru:
                print("Username sudah ada, coba yang pang!")
                break
        else:
            password_baru = input("Masukkan password baru : ")
            role = input("Daftar sebagai (admin/pengguna) : ").lower()

            if role in ['admin', 'pengguna']:
                pengguna.append([len(pengguna) + 1, username_baru, password_baru, role])
                print(f"Registrasi sebagai {role} berhasil !")
            else:
                print("Role tidak valid, harus admin atau pengguna.")

    elif pilihan == '3':
        print("Terima kasih telah menggunakan Program Pembayaran Pajak Bermotor!")
        break

    else:
        print("Pilihan tidak valid!")