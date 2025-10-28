import os
from datetime import datetime

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "ajis": {"password": "ajis123", "role": "woi"}
}

laporan = {}
log_status = {}

# VALIDASI MENU
def validasi_menu(pesan, opsi):
    try:
        pilihan = input(pesan).strip()
        if not pilihan:
            raise ValueError("Input tidak boleh kosong.")
        if pilihan not in opsi:
            raise ValueError("Pilihan tidak valid.")
        return pilihan
    except ValueError as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
        return validasi_menu(pesan, opsi)
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
        return validasi_menu(pesan, opsi)

# READ LAPORAN
def READ():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== DAFTAR LAPORAN ===")
        if not laporan:
            print("Belum ada laporan.")
        else:
            print(f"{'ID':<4} {'Lokasi':<20} {'Jenis':<12} {'Status':<15} {'Deskripsi':<25} {'Tanggal'}")
            print("-" * 100)
            for id, data in laporan.items():
                tanggal = log_status.get(id, "Belum ada")
                print(f"{id:<4} {data['lokasi']:<20} {data['jenis']:<12} {data['status']:<15} {data['deskripsi']:<25} {tanggal}")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
    input("\nKlik Enter")

# CREATE LAPORAN
def CREATE(username):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== CREATE LAPORAN ===")
        id = str(len(laporan) + 1)
        lokasi = input("Lokasi kejadian: ").strip()
        if not lokasi:
            raise ValueError("Lokasi tidak boleh kosong.")

        print("Pilih jenis masalah:\n1. Sampah\n2. Pencemaran\n3. Perusakan")
        jenis_input = input("Masukkan pilihan (1/2/3): ").strip()
        jenis_map = {"1": "sampah", "2": "pencemaran", "3": "perusakan"}
        jenis = jenis_map.get(jenis_input)

        if not jenis:
            raise ValueError("Jenis masalah tidak valid.")

        deskripsi = input("Deskripsi singkat: ").strip()
        if not deskripsi:
            raise ValueError("Deskripsi tidak boleh kosong.")

        laporan[id] = {
            "lokasi": lokasi,
            "jenis": jenis,
            "deskripsi": deskripsi,
            "status": "belum ditindak",
            "dibuat_oleh": username
        }
        log_status[id] = datetime.now().strftime("%d-%m-%Y %H:%M")
        print("\nLaporan berhasil dibuat.")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
    input("\nKlik Enter")

# UPDATE LAPORAN
def UPDATE():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== UPDATE STATUS LAPORAN ===")
        id = input("Masukkan ID laporan: ").strip()
        if not id:
            raise ValueError("ID tidak boleh kosong.")
        if id not in laporan:
            raise ValueError("ID tidak ditemukan.")

        data = laporan[id]
        print(f"\nLaporan ditemukan:\nLokasi: {data['lokasi']}\nJenis: {data['jenis']}\nDeskripsi: {data['deskripsi']}\nStatus: {data['status']}")
        print("\nPilih status baru:\n1. Belum ditindak\n2. Di proses\n3. Sudah ditindak")
        status_input = input("Masukkan pilihan (1/2/3): ").strip()
        status_map = {"1": "belum ditindak", "2": "di proses", "3": "sudah ditindak"}
        status_baru = status_map.get(status_input)

        if not status_baru:
            raise ValueError("Status tidak valid.")

        laporan[id]["status"] = status_baru
        log_status[id] = datetime.now().strftime("%d-%m-%Y %H:%M")
        print("\nStatus berhasil diperbarui.")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
    input("\nKlik Enter")

# HAPUS LAPORAN
def DELETE():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== HAPUS LAPORAN ===")
        id = input("Masukkan ID laporan: ").strip()
        if not id:
            raise ValueError("ID tidak boleh kosong.")
        if id in laporan:
            data = laporan[id]
            print(f"\nLaporan ditemukan:\nLokasi: {data['lokasi']}\nJenis: {data['jenis']}\nDeskripsi: {data['deskripsi']}\nStatus: {data['status']}")
            konfirmasi = input("\nYakin ingin menghapus laporan ini? (y/n): ").strip().lower()
            if konfirmasi == "y":
                del laporan[id]
                log_status.pop(id, None)
                print("\nLaporan berhasil dihapus.")
            elif konfirmasi == "n":
                print("\nPenghapusan dibatalkan.")
            else:
                print("\nInput tidak dikenali. Penghapusan dibatalkan.")
        else:
            raise ValueError("ID tidak ditemukan.")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
    input("\nKlik Enter")


# REGISTER
def REGISTER():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTRASI ===")
        username = input("Username: ").strip()
        password = input("Password (min 6 karakter): ").strip()

        if not username or not password:
            raise ValueError("Username dan password tidak boleh kosong.")
        if len(password) < 6:
            raise ValueError("Password terlalu pendek.")
        elif username in users:
            raise ValueError("Username sudah terdaftar.")
        else:
            users[username] = {"password": password, "role": "user"}
            print("\nRegistrasi berhasil.")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
    input("\nKlik Enter")

# LOGIN
def LOGIN():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin berhasil sebagai {role}")
            input("\nKlik Enter")
            return username, role
        else:
            raise ValueError("Username atau password salah.")
    except Exception as e:
        print(f"\nKesalahan yang terdeteksi: {e}")
        input("\nKlik Enter")
        return None, None

# MENU UTAMA
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== ^^^ SISTEM PELAPORAN SAMPAH & LINGKUNGAN ^^^ ===")
    print("1. Login\n2. Register\n3. Keluar")
    pilihan = input("Pilih menu: ").strip()

    if pilihan == "2":
        REGISTER()

    elif pilihan == "1":
        username, role = LOGIN()
        if not username:
            continue

        # ADMIN
        if role == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Tampilkan laporan\n2. Buat laporan\n3. Update status\n4. Hapus laporan\n5. Logout")
                pilihan = validasi_menu("Pilih menu: ", ["1", "2", "3", "4", "5"])

                if pilihan == "1":
                    READ()
                elif pilihan == "2":
                    CREATE(username)
                elif pilihan == "3":
                    UPDATE()
                elif pilihan == "4":
                    DELETE()
                elif pilihan == "5":
                    break

        # USER
        elif role == "user":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU PENGGUNA ===")
                print("1. Buat laporan\n2. Tampilkan laporan\n3. Logout")
                pilihan = validasi_menu("Pilih menu: ", ["1", "2", "3"])

                if pilihan == "1":
                    CREATE(username)
                elif pilihan == "2":
                    READ()
                elif pilihan == "3":
                    break

        # HEKER
        else:
            print("\nAnda Heker, ga boleh masuk.")
            input("\nKlik Enter")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan aplikasi ini.")
        break

    else:
        print("\nPilihan tidak valid.")
        input("\nKlik Enter")