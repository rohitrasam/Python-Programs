def hurdleRace(k, height):
    m = max(height)
    if k > m:
        return 0
    elif k < m:
        return m - k


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().split()))

    print(hurdleRace(k, height))

