import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "ajis": {"password": "ajis123", "role": "woi"}
}

laporan = {}

while True:
    os.system('cls')
    print("=== ^^^ SISTEM PELAPORAN SAMPAH & LINGKUNGAN ^^^ ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    # REGISTER
    if pilihan == "2":
        os.system('cls')
        print("=== ^^^ MENU REGISTRASI ^^^ ===")
        username = input("Username: ")
        password = input("Password (minimal 6 karakter): ")

        if len(password) < 6:
            print("\nMinimal Password harus 6 karakter")
        elif username in users:
            print("\nUsername sudah ada.")
        else:
            users[username] = {"password": password, "role": "user"}
            print("\nRegistrasi berhasil")
        input("\nKlik Enter")

    # LOGIN
    elif pilihan == "1":
        os.system('cls')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin berhasil sebagai {role}")
            print(f"Halo {username}!")
            input("\nKlik Enter")
        else:
            print("\nUsername atau password salah.")
            input("\nKlik Enter")
            continue

        # ADMIN MENU
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
                        for id, data in laporan.items():
                            print(f"{id:<4} {data['lokasi']:<20} {data['jenis']:<12} {data['status']:<15} {data['deskripsi']}")
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

                    jenis_map = {"1": "sampah", "2": "pencemaran", "3": "perusakan"}
                    jenis = jenis_map.get(jenis_input)

                    if not jenis:
                        print("\nPilihan tidak valid.")
                        input("\nKlik Enter")
                        continue

                    deskripsi = input("Deskripsi singkat: ")
                    laporan[id] = {
                        "lokasi": lokasi,
                        "jenis": jenis,
                        "deskripsi": deskripsi,
                        "status": "belum ditindak"
                    }
                    print("\nLaporan berhasil dibuat.")
                    input("\nKlik Enter")

                elif pilihan == "3":
                    os.system('cls')
                    print("=== UPDATE STATUS LAPORAN ===")
                    id = input("Masukkan ID laporan: ")

                    if id in laporan:
                        data = laporan[id]
                        print(f"\nLaporan ditemukan:")
                        print(f"Lokasi: {data['lokasi']}")
                        print(f"Jenis: {data['jenis']}")
                        print(f"Deskripsi: {data['deskripsi']}")
                        print(f"Status saat ini: {data['status']}\n")

                        print("Pilih status baru:")
                        print("1. Belum ditindak")
                        print("2. Di proses")
                        print("3. Sudah ditindak")
                        status_input = input("Masukkan pilihan (1/2/3): ")

                        status_map = {"1": "belum ditindak", "2": "di proses", "3": "sudah ditindak"}
                        status_baru = status_map.get(status_input)

                        if status_baru:
                            laporan[id]["status"] = status_baru
                            print("\nStatus berhasil diperbarui.")
                        else:
                            print("\nPilihan tidak valid.")
                    else:
                        print("\nID tidak ditemukan.")
                    input("\nKlik Enter")

                elif pilihan == "4":
                    os.system('cls')
                    print("=== HAPUS LAPORAN ===")
                    id = input("Masukkan ID laporan: ")
                    if id in laporan:
                        del laporan[id]
                        print("\nLaporan berhasil dihapus.")
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

        # USER MENU
        elif role == "user":
            while True:
                os.system('cls')
                print("=== ^^^ MENU PENGGUNA ^^^ ===")
                print("1. Create laporan")
                print("2. Tampilkan laporan")
                print("3. LogOut")
                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    os.system('cls')
                    print("=== ^^^ CREATE LAPORAN ^^^ ===")
                    id = str(len(laporan) + 1)
                    lokasi = input("Lokasi kejadian: ")

                    print("Pilih jenis masalah:")
                    print("1. Sampah")
                    print("2. Pencemaran")
                    print("3. Perusakan")
                    jenis_input = input("Masukkan pilihan (1/2/3): ")

                    jenis_map = {"1": "sampah", "2": "pencemaran", "3": "perusakan"}
                    jenis = jenis_map.get(jenis_input)

                    if not jenis:
                        print("\nPilihan tidak valid.")
                        input("\nKlik Enter")
                        continue

                    deskripsi = input("Deskripsi singkat: ")
                    laporan[id] = {
                        "lokasi": lokasi,
                        "jenis": jenis,
                        "deskripsi": deskripsi,
                        "status": "belum ditindak"
                    }
                    print("\nLaporan berhasil dibuat.")
                    input("\nKlik Enter")

                elif pilihan == "2":
                    os.system('cls')
                    print("=== ^^^ DAFTAR LAPORAN ^^^ ===")
                    if not laporan:
                        print("Tidak ada laporan.")
                    else:
                        print(f"{'ID':<4} {'Lokasi':<20} {'Jenis':<12} {'Status':<15} {'Deskripsi'}")
                        print("-" * 80)
                        for id, data in laporan.items():
                            print(f"{id:<4} {data['lokasi']:<20} {data['jenis']:<12} {data['status']:<15} {data['deskripsi']}")
                    input("\nKlik Enter")

                elif pilihan == "3":
                    validate = input("Yakin ingin logout? (y/n): ").lower()
                    if validate == 'y':
                        break
                    elif validate not in ['y', 'n']:
                        print("\nInput tidak valid.")
                        input("\nKlik Enter")
                else:
                    print("\nMenu tidak valid.")
                    input("\nKlik Enter")

        # HEKER GILA
        else:
            print("\nAnda Heker, Ya? Maaf ga bisa masuk.")
            input("\nKlik Enter")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan aplikasi ini.")
        break

    else:
        print("\nMenu tidak valid.")
        input("\nKlik Enter")
