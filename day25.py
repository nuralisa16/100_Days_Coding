a = int(input("Masukkan angka1: "))
b = int(input("Masukkan angka 2: "))

while a != b:
    if a > b :
        print("Angka1 lebih besar dari angka2.")
    else:
        print("Angka1 lebih kecil dari angka2.")
    a = int(input("Masukkan angka1: "))
    b = int(input("Masukkan angka2: "))

print("Angka1 sama dengan angka2.")
