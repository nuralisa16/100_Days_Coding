arr = [2, 4, 6, 8, 10]
for i in range(len(arr)):
    factorial = 1
    for j in range(1, arr[i] + 1):
        factorial *= j
    arr[i] = factorial
print("Hasil:", arr)


