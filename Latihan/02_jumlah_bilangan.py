# Latihan 2: Jumlah 1 sampai n
# Input: Bilangan bulat positif n
# Proses: Mengakumulasi penjumlahan dari 1 hingga n menggunakan for
# Kondisi Berhenti: i mencapai n + 1
# Output: Jumlah total penjumlahan

n = int(input("n: "))
total = 0
for i in range(1, n + 1):
    total += i

print(f"Jumlah: {total}")