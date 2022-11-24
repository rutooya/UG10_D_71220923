print("\(^o^) Selamat datang di Kalkulator Sederhana (^o^)/")

print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("Ketik 6 untuk menghitung pemangkatan.")

pilihan = int(input("Masukkan pilihan Anda: "))
pertama = int(input("Masukkan bilangan pertama: "))
kedua = int(input("Masukkan bilangan kedua: "))
if(pilihan==1):
    jumlah = pertama+kedua
    print("Hasil dari", pertama, "ditambahkan dengan", kedua, "adalah", jumlah)
elif(pilihan==2):
    jumlah = pertama-kedua
    print("Hasil dari", pertama, "dikurangkan dengan", kedua, "adalah", jumlah)
elif(pilihan==3):
    jumlah = pertama*kedua
    print("Hasil dari", pertama, "dikalikan dengan", kedua, "adalah", jumlah)
elif(pilihan==4):
    jumlah = pertama/kedua
    print("Hasil dari", pertama, "dibagi dengan", kedua, "adalah", jumlah)
elif(pilihan==5):
    jumlah = pertama%kedua
    print("Hasil dari", pertama, "dimodulus dengan", kedua, "adalah", jumlah)
else:
    jumlah = pertama**kedua
    print("Hasil dari", pertama, "dipangkatkan dengan", kedua, "adalah", jumlah)