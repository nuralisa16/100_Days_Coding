usia = int(input("Masukkan usia kamu: "))

if 15 <= usia <= 20:
    print("Anda masih remaja")
elif 21 <= usia <= 40:
    print("Anda sudah dewasa")
elif 41 <= usia <= 60:
    print("Anda sudah tua")
else:
    print("Usiamu tidak masuk kategori")

