arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):
    arr[i] = arr[i] ** 2
print("hasil :", arr)
total = 0
for num in arr:
    total += num
print("Total penjumlahan elemen array:", total)
