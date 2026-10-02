# Latihan 3: Validasi Input Berulang
# Input: Nilai ujian (float)
# Proses: Meminta ulang input selama nilai < 0 atau nilai > 100 menggunakan while
# Kondisi Berhenti: Nilai berada di rentang 0 sampai 100 (False pada kondisi while)
# Output: Konfirmasi nilai valid yang diterima

nilai = float(input("Nilai 0-100: "))
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")
