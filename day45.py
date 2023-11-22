gaji = float(input("Masukkan gaji per bulan: "))
jenis_pekerjaan = input("Masukkan jenis pekerjaan: ")

if gaji >= 5000000 and jenis_pekerjaan != "PNS":
    pajak = 0.1 * gaji
    print("Pajak 10%")
elif gaji >= 3000000:
    if jenis_pekerjaan == "PNS":
        pajak = 0.15 * gaji
        print("PNS Tambah 5%")
    else:
        pajak = 0.05 * gaji
        print("Pajak 5%")
else:
    pajak = 0
    print("Tidak ada pajak")

gaji_bersih = gaji - pajak
print("Penghasilan bersih per bulan:", gaji_bersih)
