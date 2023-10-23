apel = int(input("masukkan buah apel yang dibeli: "))
harga = 15000  # harga per kilo
total = harga * apel  

if apel >= 20 :
    diskon = total * (30/ 100)  
    jumlah = total - diskon 
    print("Total belanja anda: ", jumlah)
    print("Anda mendapatkan diskon 30%")
else:
    print("Anda tidak mendapatkan diskon ")
    print("Total belanja anda: ", total)
