def jumlah_bilangan_ganjil(n):
  jumlah = 0
  for i in range(1, n + 1):
    if i % 2 != 0:
      jumlah += 1
  return jumlah

print(jumlah_bilangan_ganjil(100))