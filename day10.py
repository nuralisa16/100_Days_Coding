#aritmatika
a = int(input("masukkan angka pertama : "))
b = int(input("masukkan angka kedua : "))

pilihan = input("masukkan pilihan : ")

if pilihan == "penjumlahan" :
    hasil = a+b
    print("hasil : ",hasil)
elif pilihan == "perkalian" :
    hasil = a*b
    print("hasil : ",hasil)
elif pilihan == "pengurangan":
    hasil = a-b
    print("hasil : ",hasil)
elif pilihan == "pembagian" :
    hasil = a/b
    print("hasil : ",hasil)
else :
    print("pilihan tidak adaa")
    
