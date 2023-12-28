def jumlahkan_bilangan(a, b):
    hasil = a * b
    return hasil

bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

total = jumlahkan_bilangan(bilangan1, bilangan2)

print("Hasil penjumlahan:", total)
