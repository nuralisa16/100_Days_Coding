angka = int(input("Masukkan angka: "))
Genap = 0
Ganjil = 0

for i in range(1, angka + 1):
    if i % 2 == 0:
        Genap += i
        print("Angka genap : " ,i)
    else:
        Ganjil += i
        print("Angka ganjil : ",i)

print("Total angka genap:", Genap)
print("Total angka ganjil:", Ganjil)

