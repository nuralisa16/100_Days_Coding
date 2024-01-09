def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def kombinasi(n, r):
    return faktorial(n) / (faktorial(r) * faktorial(n-r))

def hitung(a, b, c):
    hasil = (a**2 + b**3) * kombinasi(c, 2)
    return hasil
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

hasil_perhitungan = hitung(a, b, c)
print(f"Hasil perhitungan : {hasil_perhitungan}")
