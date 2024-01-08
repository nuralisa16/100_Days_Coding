def hitung_luas_pangkat(sisi, pangkat):
    luas = sisi ** pangkat
    return luas

def hitung_keliling_pangkat(sisi, pangkat):
    keliling = 4 * sisi ** (pangkat-1)
    return keliling
sisi = float(input("Masukkan panjang sisi bangun datar: "))
pangkat = int(input("Masukkan pangkat bangun datar: "))

luas = hitung_luas_pangkat(sisi, pangkat)
keliling = hitung_keliling_pangkat(sisi, pangkat)

print(f"Luas bangun datar pangkat adalah: {luas}")
print(f"Keliling bangun datar pangkat adalah: {keliling}")
