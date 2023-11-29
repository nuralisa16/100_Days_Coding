a = int(input("masukkan nilai a : "))
b = int(input("masukkan nilai b : "))

total = a * b
if total % 2 == 0:
    total -=2
    print(total)
else :
    total+=1
    print(total)