angka= int(input("masukkan angka : "))
genap =0
ganjil =0
for i in range(1,angka+1):
	if i % 2 == 0:
	    genap+=1
	else:
		ganjil +=1
print("total genap : ",genap)
print("total ganjil  : ",ganjil)