#gaji bersih karyawan
gajiLembur_Perjam = 55000
gaji_pokok = int(input("masukkan gaji : "))
lama_lembur = int(input("masukkan lama lembur : "))

gaji_lembur = gajiLembur_Perjam * lama_lembur
gaji_bersih = gaji_pokok + gaji_lembur

print("gaji lembur anda : ",gaji_lembur)
print("gaji bersih anda : ",gaji_bersih)
