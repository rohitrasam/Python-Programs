def fairRation(b):
    breads = 0
    m = len(b)

    for i in range(m-1):
        if b[i] % 2 == 1:
            breads += 2
            b[i+1] += 1

    if b[n-1] % 2 == 1:
        print('NO')
    else:
        print(breads)


if __name__ == '__main__':
    n = int(input())

    b = list(map(int, input().split()))

    fairRation(b)