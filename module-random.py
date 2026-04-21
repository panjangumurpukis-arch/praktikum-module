import random

print(random.random())
print(random.randint(1, 10))

nama = ["ambatusam", "saski", "oze"]
print(random.choice(nama))

random.shuffle(nama)
print(nama)