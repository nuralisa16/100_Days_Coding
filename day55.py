def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

nilai_n= int(input("masukkan nilai n : "))
print(factorial(nilai_n))