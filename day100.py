def buat_array(ukuran):
    array = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(ukuran)]
    return array

def temukan_terbesar(array):
    terbesar = max(array, default=None)
    return terbesar

ukuran_array = int(input("Masukkan ukuran array: "))
array = buat_array(ukuran_array)
bilangan_terbesar = temukan_terbesar(array)
print(f"Bilangan terbesar dalam array: {bilangan_terbesar}")

