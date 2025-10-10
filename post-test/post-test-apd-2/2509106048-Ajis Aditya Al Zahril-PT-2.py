suhu = [27, 33, 46, 55, 67, 92]

f1 = (suhu[0] * 9/5) + 32
f2 = (suhu[1] * 9/5) + 32

k1 = suhu[2] + 273.15
k2 = suhu[3] + 273.15

r1 = suhu[4] * 4/5
r2 = suhu[5] * 4/5

jumlah = f1 + f2 + k1 + k2 + r1 + r2
rata2 = jumlah / len(suhu)
NIM = 48
bolean = NIM < rata2

print("List suhu: ", suhu)
print("fahrenheit: ", f1, " | ", f2)
print("kelvin: ", k1, " | ", k2)
print("reamur: ", r1, " | ", r2)
print("jumlah: ", jumlah)
print("rata-rata: ", rata2)
print("NIM: ", NIM)
print("bolean: ", bolean)

print("suhu 46 sampai 92: ", suhu[-4:])