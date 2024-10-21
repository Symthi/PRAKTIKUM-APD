pengguna = {
    'admin': {'password': 'admin123', 'role': 'admin'}
}

pajak_motor = {
    1: {'jenis': 'Motor Satria', 'pajak': 250000, 'plat': 'KT 1234 LK', 'pemilik': 'Fajar'},
    2: {'jenis': 'Motor Honda', 'pajak': 300000, 'plat': 'KT 2374 AS', 'pemilik': 'Ahnaf'},
    3: {'jenis': 'Motor Scoopy', 'pajak': 500000, 'plat': 'KT 3452 SD', 'pemilik': 'Elfin'}
}

current_user = None

def login(username, password):
    global current_user
    user = pengguna.get(username)
    if user and user['password'] == password:
        current_user = username
        return user['role']
    else:
        raise ValueError("Username atau password salah!")

def tambah_motor(jenis_motor_baru, biaya_baru, plat_nomor_baru, nama_pemilik_baru):
    global pajak_motor
    motor_id = len(pajak_motor) + 1
    pajak_motor[motor_id] = {
        'jenis': jenis_motor_baru, 
        'pajak': biaya_baru, 
        'plat': plat_nomor_baru, 
        'pemilik': nama_pemilik_baru
    }

def recursive_logout(count=3):
    if count == 0:
        return True
    print(f"Logout dalam {count} detik...")
    recursive_logout(count - 1)

def lihat_motor():
    print("\n" + "-"*40)
    print(f"    DAFTAR PAJAK MOTOR (Total: {len(pajak_motor)})    ")
    print("-"*40)
    for motor_id, motor in pajak_motor.items():
        print(f"ID : {motor_id} | {motor['jenis']} | Pajak : {motor['pajak']} | Plat : {motor['plat']} | Pemilik : {motor['pemilik']}")
    print("-"*40)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka!")

def tampilkan_menu(role):
    if role == 'admin':
        print("\n" + "="*40)
        print("               MENU ADMIN         ")
        print("="*40)
        print("1. Tambah Jenis Motor")
        print("2. Lihat Daftar Pajak Motor")
        print("3. Edit Pajak Motor")
        print("4. Hapus Jenis Motor")
        print("5. Logout")
        print("="*40)
    else:
        print("\n" + "="*40)
        print("               MENU PENGGUNA        ")
        print("="*40)
        print("1. Lihat Daftar Pajak Motor")
        print("2. Bayar Pajak Motor")
        print("3. Logout")
        print("="*40)

def program_utama():
    global pengguna, pajak_motor, current_user
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

            try:
                role = login(username, password)
                print(f"\nSelamat datang, {username}!")

                while True:
                    tampilkan_menu(role)
                    pilihan_menu = input("Pilih opsi: ")

                    if role == 'admin':
                        if pilihan_menu == '1':
                            print("\n" + "-"*40)
                            print("           TAMBAH JENIS MOTOR      ")
                            print("-"*40)
                            jenis_motor = input("Masukkan jenis Motor : ")
                            pajak_motor_baru = input_int("Masukkan biaya Pajak : ")
                            plat_nomor = input("Masukkan Plat Nomor : ")
                            pemilik = input("Masukkan Nama Pemilik Motor : ")
                            tambah_motor(jenis_motor, pajak_motor_baru, plat_nomor, pemilik)
                            print("Motor berhasil ditambahkan!")

                        elif pilihan_menu == '2':
                            lihat_motor()

                        elif pilihan_menu == '3':
                            print("\n" + "-"*40)
                            print("            EDIT PAJAK MOTOR       ")
                            print("-"*40)
                            motor_id = input_int("Masukkan ID motor yang akan diedit: ")
                            pajak_baru = input_int("Masukkan biaya pajak baru: ")
                            if motor_id in pajak_motor:
                                pajak_motor[motor_id]['pajak'] = pajak_baru
                                print("Pajak motor berhasil diupdate!")
                            else:
                                print("Motor tidak ditemukan!")

                        elif pilihan_menu == '4':
                            print("\n" + "-"*40)
                            print("            HAPUS JENIS MOTOR      ")
                            print("-"*40)
                            motor_id = input_int("Masukkan ID motor yang akan dihapus: ")
                            if motor_id in pajak_motor:
                                del pajak_motor[motor_id]
                                print("Jenis motor berhasil dihapus!")
                            else:
                                print("Motor tidak ditemukan!")

                        elif pilihan_menu == '5':
                            print("Logout berhasil!")
                            recursive_logout()
                            break

                        else:
                            print("Pilihan tidak valid!")

                    else:
                        if pilihan_menu == '1':
                            lihat_motor()

                        elif pilihan_menu == '2':
                            print("\n" + "-"*40)
                            print("         PEMBAYARAN PAJAK MOTOR    ")
                            print("-"*40)
                            motor_id = input_int("Masukkan ID motor yang ingin dibayar pajaknya: ")
                            if motor_id in pajak_motor:
                                print(f"Pajak {pajak_motor[motor_id]['jenis']} sebesar {pajak_motor[motor_id]['pajak']} telah dibayar!")
                                pajak_motor[motor_id]['pajak'] = 0
                            else:
                                print("Motor tidak ditemukan!")

                        elif pilihan_menu == '3':
                            print("Logout berhasil!")
                            recursive_logout()
                            break

                        else:
                            print("Pilihan tidak valid!")

            except ValueError as e:
                print(e)

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

program_utama()