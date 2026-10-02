# Latihan 4: Menghitung Bilangan Genap
# Input: Bilangan bulat positif n
# Proses: Melakukan iterasi dari 1 sampai n, memeriksa apakah i genap menggunakan modulus, lalu mencacah
# Kondisi Berhenti: i mencapai n + 1
# Output: Banyak bilangan genap dalam rentang 1 sampai n

n = int(input("n: "))
jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap: {jumlah_genap}")