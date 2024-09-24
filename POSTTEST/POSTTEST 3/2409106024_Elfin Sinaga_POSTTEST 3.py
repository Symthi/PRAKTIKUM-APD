print("<=========================================================================================================================================>")
nama = input("Masukkan Nama Lengkap : ")
nim = input("Masukkan NIM : ")
total_pinjaman = int(input("Masukkan Total Pinjaman : "))
lama_cicilan = int(input("Masukkan Lama Cicilan (1 - 3 Tahun): "))

if lama_cicilan == 1 : 
    bunga_perbulan = (0.07 / 12) * total_pinjaman
    cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 12
elif lama_cicilan == 2:
    bunga_perbulan = (0.13 / 12) * total_pinjaman
    cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 24
elif lama_cicilan == 3:
    bunga_perbulan = (0.07 / 12) * total_pinjaman
    cicilan_bulanan = (total_pinjaman + bunga_perbulan) / 36

print(f"atas Nama {nama} dengan NIM {nim} akan melakukan pinjaman sebesar {total_pinjaman} dengan cicilannya sebesar {cicilan_bulanan:.0f}")
print("<=========================================================================================================================================>")