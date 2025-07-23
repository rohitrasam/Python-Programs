def fact(num):
    return 1 if num == 0 else num * fact(num-1)


def comb(x, r):
    return fact(x) / (fact(r)*(fact(x-r)))


def b(x, n1, p):
    return comb(n1, x) * p**x * (1 - p)**(n1 - x)


_1, n = map(int, input().split())

print(round(sum([b(i, n, _1/100) for i in range(3)]), 3))
print(round(sum([b(i, n, _1/100) for i in range(2, n + 1)]), 3))
