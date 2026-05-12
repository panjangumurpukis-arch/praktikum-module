# Spiral pelangi
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 3)
    t.right(59)

turtle.done()

# Bunga Berpola
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# for i in range(36):
#     for j in range(4):
#         t.forward(100)
#         t.right(90)
#     t.right(10)

# turtle.done()

# Bintang Berputar Warna-warni
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# colors = ["red", "blue", "green", "yellow", "purple"]

# for i in range(50):
#     t.color(colors[i % 5])
#     t.forward(150)
#     t.right(144)
#     t.right(5)

# turtle.done()

# Lingkaran spiral modern
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# for i in range(200):
#     t.circle(i)
#     t.right(10)

# turtle.done()

# Efek Ledakan
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# for i in range(36):
#     t.forward(100)
#     t.backward(100)
#     t.right(10)

# turtle.done()

# Spiral Kotak berwarna
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# colors = ["red", "green", "blue", "yellow"]

# for i in range(100):
#     t.color(colors[i % 4])
#     for j in range(4):
#         t.forward(i * 2)
#         t.right(90)
#     t.right(10)

# turtle.done()
