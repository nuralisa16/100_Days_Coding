def bandingkan_angka(angka1, angka2):
    if angka1 > angka2:
        return f"{angka1} lebih besar dari {angka2}"
    elif angka1 < angka2:
        return f"{angka1} lebih kecil dari {angka2}"
    else:
        return f"{angka1} sama dengan {angka2}"
hasil= bandingkan_angka(5, 10)
print(hasil)
