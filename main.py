from input_data import ambil_data 
from proses_nilai import hitung_rata_rata, cek_kelulusan 
nama, nilai = ambil_data() 
rata = hitung_rata_rata(nilai) 
status = cek_kelulusan(rata) 
print("\n=== HASIL ===") 
print("nama",nama)
print("nilai", nilai)
print("Rata-rata", rata)
print("status", status)