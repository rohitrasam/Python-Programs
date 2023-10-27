# Successive Approximation

from math import cos, exp, sin


g = lambda x: (x**2 + 6) / 8
dg = lambda x: x / 4

def start():
    global x1
    x1 = float(input("Enter initial guess: "))
    global accuracy 
    accuracy = float(input("Accuracy: "))

start()

while dg(x1) > 1:
    start()

x2 = g(x1)

while abs(x2 - x1) > accuracy:
    x1 = x2

    x2 = g(x1)

print(x2)



