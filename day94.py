def genap_ganjil(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def positif_negatif_nol(angka):
    if angka > 0:
        return "positif"
    elif angka < 0:
        return "negatif"
    else:
        return "nol"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if angka1 > angka2:
    print(f"{angka1} lebih besar dari {angka2}")
elif angka1 < angka2:
    print(f"{angka1} lebih kecil dari {angka2}")
else:
    print(f"{angka1} sama dengan {angka2}")

print(f"{angka1} adalah bilangan {genap_ganjil(angka1)} dan {positif_negatif_nol(angka1)}")
print(f"{angka2} adalah bilangan {genap_ganjil(angka2)} dan {positif_negatif_nol(angka2)}")
