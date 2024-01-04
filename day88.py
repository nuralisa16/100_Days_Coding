def buat_array(ukuran):
    array = []
    for i in range(1, ukuran + 1):
        array.append(i)
    return array
def cari_ganjil(array):
    print("Bilangan ganjil dalam array:")
    for angka in array:
        if angka % 2 != 0:
            print(angka)

ukuran_array = int(input("Masukkan ukuran array: "))
array = buat_array(ukuran_array)
cari_ganjil(array)
