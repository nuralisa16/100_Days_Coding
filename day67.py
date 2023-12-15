def perkalian_array(arr):
    hasil = 1
    for elemen in arr:
        hasil *= elemen
    return hasil
array = [2, 3, 4, 5]
hasil_perkalian = perkalian_array(array)
print("Hasil perkalian array:", hasil_perkalian)