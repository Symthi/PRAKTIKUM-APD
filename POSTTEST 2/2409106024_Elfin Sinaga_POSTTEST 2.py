nama = input("Masukkan Nama Lengkap =")
nim = input("Masukkan NIM = ")
beras = int(input("Masukan harga beras = "))

diskon ={
    "diskon_mawar" : 0.11,
    "diskon_sania" : 0.14,
    "diskon_maknyus" : 0.17
}

diskon_mawar = beras * diskon["diskon_mawar"]
diskon_sania = beras * diskon["diskon_sania"]
diskon_maknyus = beras * diskon["diskon_maknyus"]

mawar = beras - diskon_mawar
sania = beras - diskon_sania
maknyus = beras - diskon_maknyus

print(f"seorang mahasiswa yang bernama{nama} dengan nim {nim} ingin membeli beras seharga {beras}""\n"
      f"jika dia membeli beras mawar ia harus membayar {mawar} setelah mendepat diskon 11%""\n"
      f"jika dia membeli beras sania ia harus membayar {sania} setelah mendepat diskon 14%""\n"
      f"jika dia membeli beras maknyus ia harus membayar {maknyus} setelah mendepat diskon 17%""\n"
)