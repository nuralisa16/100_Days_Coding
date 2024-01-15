def buat_array(ukuran):
    array = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(ukuran)]
    return array

def hitung_rata_ganjil(array):
    ganjil = [angka for angka in array if angka % 2 != 0]
    rata_ganjil = sum(ganjil) / len(ganjil) if ganjil else 0
    return rata_ganjil

ukuran_array = int(input("Masukkan ukuran array: "))
array = buat_array(ukuran_array)
rata_ganjil = hitung_rata_ganjil(array)
print(f"Rata-rata bilangan ganjil dalam array: {rata_ganjil}")
