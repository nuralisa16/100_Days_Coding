def bagi_tiga_lima(angka):
    if angka % 3 == 0 and angka % 5 == 0:
        return "habis dibagi 3 dan 5"
    elif angka % 3 == 0:
        return "habis dibagi 3"
    elif angka % 5 == 0:
        return "habis dibagi 5"
    else:
        return "tidak habis dibagi 3 atau 5"

def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka/2)+1):
            if (angka % i) == 0:
                return "bukan bilangan prima"
                break
        else:
            return "bilangan prima"
    else:
        return "bukan bilangan prima"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if angka1 > angka2:
    print(f"{angka1} lebih besar dari {angka2}")
elif angka1 < angka2:
    print(f"{angka1} lebih kecil dari {angka2}")
else:
    print(f"{angka1} sama dengan {angka2}")

print(f"{angka1} {bagi_tiga_lima(angka1)} dan {cek_prima(angka1)}")
print(f"{angka2} {bagi_tiga_lima(angka2)} dan {cek_prima(angka2)}")
