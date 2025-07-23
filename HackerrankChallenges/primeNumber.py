import math as m
n = int(input('Enter a number: '))
for i in range(2,m.floor(m.sqrt(n) +1)):
    if n % i == 0:
        print("It is not a prime number.")
        break
else:
    print("It is a prime number.")
