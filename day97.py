def hitung_genap(array):
    jumlah_genap = sum(1 for angka in array if angka % 2 == 0)
    return jumlah_genap

ukuran_array = int(input("Masukkan ukuran array: "))
array = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(ukuran_array)]
jumlah_genap = hitung_genap(array)
print(f"Jumlah bilangan genap dalam array: {jumlah_genap}")

