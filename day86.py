while True:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    pilihan = input("Masukkan pilihan : ")
    if pilihan == '1':
        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)
    elif pilihan == '2':
        hasil = angka1 - angka2
        print("Hasil pengurangan:", hasil)
    elif pilihan == '3':
        hasil = angka1 * angka2
        print("Hasil perkalian:", hasil)
    elif pilihan == '4':
         hasil = angka1 / angka2
         print("Hasil pembagian:", hasil)
    else:
        print("Pilihan tidak valid")
