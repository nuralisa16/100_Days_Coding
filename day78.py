def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan genap"
    else:
        return f"{angka} adalah bilangan ganjil"

hasil= cek_ganjil_genap(7)
print(hasil)
