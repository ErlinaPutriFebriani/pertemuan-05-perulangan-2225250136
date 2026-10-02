# Latihan 1: Tabel Perkalian
# Input: Bilangan bulat n
# Proses: Menampilkan perkalian n dari 1 sampai 10 menggunakan for
# Kondisi Berhenti: i mencapai 11 (batas range)
# Output: Baris perkalian n x i

n = int(input("Bilangan: "))
for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")