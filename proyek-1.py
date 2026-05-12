import random

angka = random.randint(1, 10)

tebakan = int(input("tebak angka (1-10): "))

if tebakan == angka :
    print("❤️ benar!")

else:
    print("💔salah, jawabannya:", angka)