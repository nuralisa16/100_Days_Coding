array1 = [2, 4, 6, 8]
array2 = [1, 3, 5, 7]
# Membuat array hasil perkalian
hasil = [a * b for a, b in zip(array1, array2)]
print("Array 1:", array1)
print("Array 2:", array2)
print("Hasil Perkalian:", hasil)
