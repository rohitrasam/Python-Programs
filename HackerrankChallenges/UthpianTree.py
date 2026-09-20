def utopianTree(n):
    i = 1
    for j in range(1, n+1):
        if j % 2 == 0:
            i += 1
        else:
            i *= 2

    return i


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(utopianTree(n))
