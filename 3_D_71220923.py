tahun = int(input("Masukkan Tahun: "))
tahun
if(tahun/4==0):
    akhir=tahun/4==0
    print(tahun, "merupakan Tahun Kabisat", akhir)
elif(tahun/400==0):
    akhir=tahun/400==0
    print(tahun, "merupakan Tahun Kabisat", akhir)
else:
    print(tahun, "bukan merupakan Tahun Kabisat")