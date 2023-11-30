batas = int(input("masukkan batas : "))

if batas % 2 == 0:
    print("angka genap")
else:
    for i in range(1,batas):
        if i % 2 ==0:
            print(i)