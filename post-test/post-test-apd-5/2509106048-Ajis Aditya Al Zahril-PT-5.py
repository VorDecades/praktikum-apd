import os

laporan = []
users = [["admin", "admin123", "admin"], ["user", "user123", "user"], ["ajis", "ajis123", "woi"]]

while True:
    os.system('cls')
    print("=== ^^^ SISTEM PELAPORAN SAMPAH & LINGKUNGAN ^^^ ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")


    #REGISTER
    if pilihan == "2":
        while True:
            os.system('cls')
            print("=== ^^^ MENU REGISTRASI ^^^ ===")
            username = input("Username: ")
            password = input("Password (minimal 6 karakter): ")
            if len(password) < 6:
                print('\nMinimal Password harus 6 karakter')
                input('\nKlik Enter')
                continue

            duplikat = False
            for user in users:
                if user[0] == username:
                    print("\nusername sudah ada.")
                    duplikat = True
                    input("\nKlik Enter")
                    continue
            if not duplikat:
                users.append([username, password, "user"])
                print("\nRegistrasi berhasil")
                input("\nKlik Enter")
                break

    elif pilihan == "1":
        os.system('cls')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        role = None
        for user in users:
            if user[0] == username and user[1] == password:
                role = user[2]
                print(f"\nLogin berhasil sebagai {role}")
                print(f"Halo {user[0]}!")
                break
        if not role:
            print("\nUsername atau password salah.")
            input("\nKlik Enter")
            continue
        input("\nKlik Enter")

        #ADMIN
        if role == "admin":
            while True:
                os.system('cls')
                print("=== MENU ADMIN ===")
                print("1. Tampilkan laporan")
                print("2. Buat laporan")
                print("3. Update status laporan")
                print("4. Hapus laporan")
                print("5. Logout")
                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    os.system('cls')
                    print("=== DAFTAR LAPORAN ===")
                    if not laporan:
                        print("Belum ada laporan.")
                    else:
                        print(f"{'ID':<4} {'Lokasi':<20} {'Jenis':<12} {'Status':<15} {'Deskripsi'}")
                        print("-" * 80)
                        for lapor in laporan:
                            print(f"{lapor[0]:<4} {lapor[1]:<20} {lapor[2]:<12} {lapor[4]:<15} {lapor[3]}")
                    input("\nKlik Enter")

                elif pilihan == "2":
                    os.system('cls')
                    print("=== CREATE LAPORAN ===")
                    id = str(len(laporan) + 1)
                    lokasi = input("Lokasi kejadian: ")

                    print("Pilih jenis masalah:")
                    print("1. Sampah")
                    print("2. Pencemaran")
                    print("3. Perusakan")
                    jenis_input = input("Masukkan pilihan (1/2/3): ")

                    if jenis_input == "1":
                        jenis = "sampah"
                    elif jenis_input == "2":
                        jenis = "pencemaran"
                    elif jenis_input == "3":
                        jenis = "perusakan"
                    else:
                        print("\nPilihan tidak valid.")
                        input("\nKlik Enter")
                        continue

                    deskripsi = input("Deskripsi singkat: ")
                    status = "belum ditindak"
                    laporan.append([id, lokasi, jenis, deskripsi, status])
                    print("\nLaporan berhasil dibuat.")
                    input("\nKlik Enter")

                elif pilihan == "3":
                    os.system('cls')
                    print("=== UPDATE STATUS LAPORAN ===")
                    id = input("Masukkan ID laporan: ")
                    found = False

                    for lapor in laporan:
                        if lapor[0] == id:
                            print(f"\nLaporan ditemukan:")
                            print(f"Lokasi: {lapor[1]}")
                            print(f"Jenis: {lapor[2]}")
                            print(f"Deskripsi: {lapor[3]}")
                            print(f"Status saat ini: {lapor[4]}\n")

                            print("Pilih status baru:")
                            print("1. Belum ditindak")
                            print("2. Di proses")
                            print("3. Sudah ditindak")
                            pilihan = input("\nMasukkan pilihan (1/2/3): ")

                            if pilihan == "1":
                                lapor[4] = "belum ditindak"
                            elif pilihan == "2":
                                lapor[4] = "di proses"
                            elif pilihan == "3":
                                lapor[4] = "sudah ditindak"
                            else:
                                print("\nPilihan tidak valid.")
                                input("\nKlik Enter")
                                break

                            print("\nStatus berhasil diperbarui.")
                            found = True
                            break

                    if not found:
                        print("\nID tidak ditemukan.")
                    input("\nKlik Enter")

                elif pilihan == "4":
                    os.system('cls')
                    print("=== HAPUS LAPORAN ===")
                    id = input("Masukkan ID laporan: ")
                    for i in range(len(laporan)):
                        if laporan[i][0] == id:
                            del laporan[i]
                            print("\nLaporan berhasil dihapus.")
                            break
                    else:
                        print("\nID tidak ditemukan.")
                    input("\nKlik Enter")

                elif pilihan == "5":
                    validate = input("Yakin ingin logout? (y/n): ").lower()
                    if validate == 'y':
                        break
                    elif validate not in ['y', 'n']:
                        print("\nInput tidak valid.")
                        input("\nKlik Enter")
                else:
                    print("\nInput tidak valid.")
                    input("\nKlik Enter")

        #USER
        elif role == "user":
            while True:
                os.system('cls')
                print("=== ^^^ MENU PENGGUNA ^^^ ===")
                print("1. Create laporan")
                print("2. Tampilkan laporan")
                print("3. LogOut")
                pilihan = input("\nPilih menu: ")

                if pilihan == "1":
                    os.system('cls')
                    print("=== ^^^ CREATE LAPORAN ^^^ ===")
                    id = str(len(laporan) + 1)
                    lokasi = input("Lokasi kejadian: ")

                    print("Pilih jenis masalah: ")
                    print("1. Sampah")
                    print("2. Pencemaran")
                    print("3. Perusakan")
                    jenis_input = input("\nMasukkan pilihan (1/2/3): ")

                    if jenis_input == "1":
                        jenis = "sampah"
                    elif jenis_input == "2":
                        jenis = "pencemaran"
                    elif jenis_input == "3":
                        jenis = "perusakan"
                    else:
                        print("\nPilihan tidak valid.")
                        input("\nKlik Enter")
                        continue

                    deskripsi = input("Deskripsi singkat: ")
                    status = "belum ditindak"
                    laporan.append([id, lokasi, jenis, deskripsi, status])
                    print("\nLaporan berhasil dibuat.")
                    input("\nKlik Enter")

                elif pilihan == "2":
                    os.system('cls')
                    print("=== ^^^ DAFTAR LAPORAN ^^^ ===")
                    if not laporan:
                        print("Tidak ada laporan")
                    else:
                        print(f"{'ID':<4} {'Lokasi':<20} {'Jenis':<12} {'Status':<15} {'Deskripsi'}")
                        print("-" * 80)
                        for lapor in laporan:
                            print(f"{lapor[0]:<4} {lapor[1]:<20} {lapor[2]:<12} {lapor[4]:<15} {lapor[3]}")
                    input("\nKlik Enter")

                elif pilihan == "3":
                    validate = input("Yakin ingin logout? (y/n): ").lower()
                    if validate == 'y':
                        break
                    elif validate not in ['y', 'n']:
                        print("\nInput tidak valid.")
                        input("\nKlik Enter")
                else:
                    print("\nMenu tidak valid")
                    input("\nKlik Enter")
        else :
            print("\nAnda Heker, Ya? Maaf ga bisa masuk.")
            input("\nKlik Enter")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan aplikasi ini")
        break

    else:
        print("\nMenu tidak valid.")
        input("\nKlik Enter")