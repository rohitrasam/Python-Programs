def repeatedString(s, n):
    q = n // len(s)
    r = n % len(s)
    x1 = q * s.count('a')
    x2 = s[:r].count('a')
    print(x1 + x2)


if __name__ == '__main__':
    s = input()
    n = int(input())

    repeatedString(s, n)
