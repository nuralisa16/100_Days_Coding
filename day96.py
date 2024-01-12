def kuadrat_sempurna(angka):
    if angka >= 0 and (angka**0.5).is_integer():
        return "merupakan kuadrat sempurna"
    else:
        return "bukan kuadrat sempurna"
def cek_fibonacci(angka):
    a, b = 0, 1
    while b < angka:
        a, b = b, a + b
    return "termasuk dalam deret Fibonacci" if b == angka else "bukan dalam deret Fibonacci"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if angka1 > angka2:
    print(f"{angka1} lebih besar dari {angka2}")
elif angka1 < angka2:
    print(f"{angka1} lebih kecil dari {angka2}")
else:
    print(f"{angka1} sama dengan {angka2}")


print(f"{angka1} {kuadrat_sempurna(angka1)} dan {cek_fibonacci(angka1)}")
print(f"{angka2} {kuadrat_sempurna(angka2)} dan {cek_fibonacci(angka2)}")
