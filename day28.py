def persegiPanjang(panjang, lebar):
    luas = panjang * lebar
    return luas

panjang = float(input("Masukkan panjang persegi : "))
lebar = float(input("Masukkan lebar persegi: "))

hasil = persegiPanjang(panjang, lebar)
print("Luas persegi panjang adalah:", hasil)
