panjang = int(input("panjang: "))
teks = []
for i in range(panjang):
	nama = input("nama: ")
	teks.append(nama)
teks.sort(reverse=True)
print(teks)