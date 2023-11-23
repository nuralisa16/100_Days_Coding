print("[1.] Vivo")
print("[2.] Oppo")
print("[3.] Samsung")
merek_hp= input("Pilih merek HP : ")
Hp = ""
harga_hp = 0
diskon = 0
if merek_hp == "1":
    Hp = "Vivo"
    harga_hp = 3000000
    print("[1.] ", Hp)
    print("Rp.",harga_hp)
elif merek_hp== "2":
    Hp = "Oppo"
    harga_hp= 4000000
    print("[2.] ", Hp)
    print("Rp.",harga_hp)
elif merek_hp== "3":
    Hp = "Samsung"
    harga_hp = 5000000
    print("[3.]", Hp)
    print("Rp.",harga_hp)
else:
    print("Pilihan tidak ada")

if Hp:
    kartu_member = input("Apakah Anda memiliki kartu member? : ")

    if kartu_member == "Ya":
        nomor_member = input("Masukkan nomor member: ")
        diskon = 0.05
        print("Anda mendapatkan diskon 5%")
    elif kartu_member == "Tidak":
        diskon = 0
        print("Anda tidak mendapatkan diskon.")
    else:
        print("Pilihan tidak ada")

total_diskon = harga_hp * diskon
total_bayar = harga_hp - total_diskon
print("Total diskon: ", total_diskon)
print("Total bayar: ", total_bayar)


