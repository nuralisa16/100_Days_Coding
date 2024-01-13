def buat_array(ukuran):
    array = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(ukuran)]
    return array

def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka/2)+1):
            if (angka % i) == 0:
                return False
        else:
            return True
    else:
        return False

def cek_prima_array(array):
    print("Bilangan prima dalam array:")
    for angka in array:
        if cek_prima(angka):
            print(angka)

ukuran_array = int(input("Masukkan ukuran array: "))
array = buat_array(ukuran_array)
cek_prima_array(array)
