def proses_array_campuran(arr_campuran):
    for elemen in arr_campuran:
        if isinstance(elemen, int):
            print(f'Ini adalah angka: {elemen}')
        elif isinstance(elemen, str):
            print(f'Ini adalah string: {elemen}')
        else:
            print('Tipe data tidak dikenal')
array_campuran = [1, 'dua', 3, 'empat', 5, 'enam']

proses_array_campuran(array_campuran)

