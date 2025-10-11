username_Acc = "ajis"
password_Acc = "048"

while True:
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password (3 digit terakhir NIM): ").strip()

    if username == "" or password == "":
        print("Username dan Password tidak boleh kosong.")
        continue
    elif username != username_Acc and password != password_Acc:
        print("Username dan Password salah.")
        continue
    elif username != username_Acc:
        print("Hanya Username yang salah.")
        continue
    elif password != password_Acc:
        print("Hanya Password yang salah.")
        continue
    else:
        print("Login berhasil!\n")
        break

A_p = 0
A_m = 0
B_p = 0
B_m = 0
AB_p = 0
AB_m = 0
O_p = 0
O_m = 0

while True:
    g = input("Masukkan golongan darah (A, B, AB, O): ").upper().strip()
    if g == "":
        print("Golongan darah tidak boleh kosong.")
        continue
    elif g != 'A' and g != 'B' and g != 'AB' and g != 'O':
        print("Golongan darah tidak valid.")
        continue

    r = input("Masukkan Rhesus (+ atau -): ").strip()
    if r == "":
        print("Rhesus tidak boleh kosong.")
        continue
    elif r != "+" and r != "-":
        print("Rhesus tidak valid.")
        continue

    kantong = input("Masukkan jumlah kantong darah: ").strip()
    if kantong == "":
        print("Jumlah kantong darah tidak boleh kosong.")
        continue
    elif not kantong.isdigit():
        print("Input harus Angka bulat positif.")
        continue
    kantong = int(kantong)
    if kantong <= 0:
        print("Jumlah kantong darah harus lebih dari 0.")
        continue

    volume = kantong * 500

    if g == "A" and r == "+":
        A_p += volume
    elif g == "A" and r == "-":
        A_m += volume
    elif g == "B" and r == "+":
        B_p += volume
    elif g == "B" and r == "-":
        B_m += volume
    elif g == "AB" and r == "+":
        AB_p += volume
    elif g == "AB" and r == "-":
        AB_m += volume
    elif g == "O" and r == "+":
        O_p += volume
    elif g == "O" and r == "-":
        O_m += volume

    ulang = input("Apakah Anda masih mau input lagi? (Y/T): ").upper().strip()
    if ulang == "T":
        break
    elif ulang != "Y":
        print("Input Ambigu. Program berhenti.")
        break

print("\n=== ^^^^ RINGKASAN HASIL DARAH ^^^^ ===")
if A_p > 0: print(f"A+ : {A_p} ml")
if A_m > 0: print(f"A- : {A_m} ml")
if B_p > 0: print(f"B+ : {B_p} ml")
if B_m > 0: print(f"B- : {B_m} ml")
if AB_p > 0: print(f"AB+ : {AB_p} ml")
if AB_m > 0: print(f"AB- : {AB_m} ml")
if O_p > 0: print(f"O+ : {O_p} ml")
if O_m > 0: print(f"O- : {O_m} ml")
