def hasil_bilangan(a, b):
    hasil = a % b
    return hasil

bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

total = hasil_bilangan(bilangan1, bilangan2)

print("Hasil sisa bagi :", total)