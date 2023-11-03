while True:
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    
    if a < b:
        for i in range(a, b +1):
            print(i)
    else:
        for n in range(a, b -1,-1):
            print(n)

      
