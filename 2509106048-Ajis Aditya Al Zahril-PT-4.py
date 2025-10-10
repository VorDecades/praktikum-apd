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

golongan_darah = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
data_darah = [0] * len(golongan_darah)

while True:
    golongan = input("Masukkan golongan darah (A, B, AB, O): ").upper().strip()
    if golongan == "":
        print("Golongan darah tidak boleh kosong.")
        continue
    elif golongan not in ["A", "B", "AB", "O"]:
        print("Golongan darah tidak valid.")
        continue
    

    rhesus = input("Masukkan Rhesus (+ atau -): ").strip()
    if rhesus == "":
        (print("Rhesus tidak boleh kosong."))
        continue
    elif rhesus not in ["+", "-"]:
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

    key = golongan + rhesus
    index = golongan_darah.index(key)
    data_darah[index] += kantong * 500

    ulang = input("Apakah Anda masih mau input lagi? (Y/T): ").upper().strip()
    if ulang == "T":
        break
    elif ulang != "Y":
        print("Input Ambigu. Program berhenti.")
        break

print("=== ^^^^ RINGKASAN HASIL DARAH ^^^^ ===")
for i in range(len(golongan_darah)):
    if data_darah[i] > 0:
        print(f"{golongan_darah[i]} : {data_darah[i]} ml")