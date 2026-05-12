import math

print("===kalkulator cerdas===")
print("1. luas lingkaran")
print("2. akar kuadrat")
print("3. pangkat")
print("4. pembulatan atas")
print("5.pembulatan bawah")

pilihan= int(input("pilih menu (1-5): "))

#1. lingkaran
if pilihan == 1:
    r = float(input("masukkan jari-jari: "))
    luas = math.pi * r * r
    print("luas lingkaran:", luas)

#2.akar
elif pilihan == 2:
    angka = float(input("masukkan angka: "))
    hasil = math.sqrt(angka)
    print("hasil:", hasil)

#3, pangkat
elif pilihan == 3:
    a = float(input("angka:"))
    b = float(input("pangkat:"))
    hasil = math.pow(a, b)
    print("hasil:", hasil)

#4. pembulatan atas
elif pilihan == 4:
    angka = float(input("masukkan angka: "))
    print("ceil:", math.ceil(angka))
    
#5 pembulatan bawah
elif pilihan ==5:
    angka = float(input("masukkan angka:"))
    print("floor:", math.floor(angka))

else:
    print("💔 pilihan tidak valid")