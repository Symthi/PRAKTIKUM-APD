pengguna = {
    'admin': {'password': 'admin123', 'role': 'admin'}
}

pajak_motor = {
    1: {'jenis': 'Motor Satria', 'pajak': 250000, 'plat': 'KT 1234 LK', 'pemilik': 'Fajar'},
    2: {'jenis': 'Motor Honda', 'pajak': 300000, 'plat': 'KT 2374 AS', 'pemilik': 'Ahnaf'},
    3: {'jenis': 'Motor Scoopy', 'pajak': 500000, 'plat': 'KT 3452 SD', 'pemilik': 'Elfin'}
}

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

        user = pengguna.get(username)

        if user and user['password'] == password:
            print(f"\nSelamat datang, {username}!")

            if user['role'] == 'admin':
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
                        try:
                            biaya_baru = int(input("Masukkan biaya Pajak : "))
                        except ValueError:
                            print("Biaya pajak harus berupa angka!")
                            continue
                        plat_nomor_baru = input("Masukkan Plat Nomor : ")
                        nama_pemilik_baru = input("Masukkan Nama Pemilik Motor : ")

                        motor_id = max(pajak_motor.keys()) + 1
                        pajak_motor[motor_id] = {
                            'jenis': jenis_motor_baru, 
                            'pajak': biaya_baru, 
                            'plat': plat_nomor_baru, 
                            'pemilik': nama_pemilik_baru
                        }
                        print("Motor berhasil ditambahkan!")

                    elif pilihan_admin == '2':
                        print("\n" + "-"*40)
                        print(f"    DAFTAR PAJAK MOTOR (Total: {len(pajak_motor)})    ")
                        print("-"*40)
                        for motor_id, motor in pajak_motor.items():
                            print(f"ID : {motor_id} | {motor['jenis']} | Pajak : {motor['pajak']} | Plat : {motor['plat']} | Pemilik : {motor['pemilik']}")
                        print("-"*40)

                    elif pilihan_admin == '3':
                        print("\n" + "-"*40)
                        print("            EDIT PAJAK MOTOR       ")
                        print("-"*40)
                        try:
                            id_edit = int(input("Masukkan ID motor yang akan diedit : "))
                            if id_edit in pajak_motor.keys():
                                motor = pajak_motor[id_edit]
                                try:
                                    motor['pajak'] = int(input(f"Masukkan biaya baru (sebelumnya : {motor['pajak']}): "))
                                    print("Berhasil di Update!")
                                except ValueError:
                                    print("Biaya pajak harus berupa angka!")
                            else:
                                print("Jenis motor tidak ditemukan!")
                        except ValueError:
                            print("ID harus berupa angka!")

                    elif pilihan_admin == '4':
                        print("\n" + "-"*40)
                        print("            HAPUS JENIS MOTOR      ")
                        print("-"*40)
                        try:
                            id_hapus = int(input("Masukkan ID motor yang akan dihapus : "))
                            if id_hapus in pajak_motor.keys():
                                pajak_motor.pop(id_hapus)
                                print("Jenis motor berhasil dihapus!")
                            else:
                                print("Jenis motor tidak ditemukan!")
                        except ValueError:
                            print("ID harus berupa angka!")

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
                        print(f"    DAFTAR PAJAK MOTOR (Total: {len(pajak_motor)})    ")
                        print("-"*40)
                        for motor_id, motor in pajak_motor.items():
                            print(f"ID : {motor_id} | {motor['jenis']} | Pajak : {motor['pajak']} | Plat : {motor['plat']} | Pemilik : {motor['pemilik']}")
                        print("-"*40)

                    elif pilihan_pengguna == '2':
                        print("\n" + "-"*40)
                        print("         PEMBAYARAN PAJAK MOTOR    ")
                        print("-"*40)
                        try:
                            id_pajak = int(input("Masukkan ID motor yang ingin dibayar pajaknya : "))
                            if id_pajak in pajak_motor:
                                motor = pajak_motor[id_pajak]
                                print(f"Pajak {motor['jenis']} sebesar {motor['pajak']} telah dibayar!")
                            else:
                                print("Jenis motor tidak ditemukan!")
                        except ValueError:
                            print("ID harus berupa angka!")

                    elif pilihan_pengguna == '3':
                        print("Logout berhasil!")
                        break
                    else:
                        print("Pilihan tidak valid!")
        else:
            print("Username atau password salah!")

    elif pilihan == '2':
        print("\n" + "-"*40)
        print("           REGISTRASI PENGGUNA        ")
        print("-"*40)
        username_baru = input("Masukkan username baru : ")

        if username_baru in pengguna.keys():
            print("Username sudah ada, coba yang lain!")
        else:
            password_baru = input("Masukkan password baru : ")
            role = input("Daftar sebagai (admin/pengguna) : ").lower()

            if role in ['admin', 'pengguna']:
                pengguna[username_baru] = {'password': password_baru, 'role': role}
                print(f"Registrasi sebagai {role} berhasil!")
            else:
                print("Role tidak valid, harus admin atau pengguna.")

    elif pilihan == '3':
        print("Terima kasih telah menggunakan Program Pembayaran Pajak Bermotor!")
        break

    else:
        print("Pilihan tidak valid!")