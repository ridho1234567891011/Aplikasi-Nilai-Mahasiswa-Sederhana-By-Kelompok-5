from input_data import ambil_data 
from proses_nilai import hitung_rata_rata, cek_kelulusan 
nama, nilai = ambil_data() 
rata = hitung_rata_rata(nilai) 
status = cek_kelulusan(rata) 
print("\n=== HASIL ===") 
print("Mama : ",nama)
print("Nilai : ", nilai)
print("Rata-rata : ", rata)
print("status : ", status)