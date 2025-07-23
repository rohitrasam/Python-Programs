def stones(n, a, b):
    result = set()

    for i in range(n):
        s = i * a + (n-1 - i) * b
        result.add(s)

    print(*sorted(list(result)))


if __name__ == '__main__':

    T = int(input())

    for _ in range(T):
        n = int(input())
        a = int(input())
        b = int(input())

        stones(n, a, b)
