def chocolateFeast(n, c, m):
    count = 0
    bars = n // c
    wrappers = bars
    while bars > 0:
        count += bars
        bars = wrappers // m
        wrappers = (wrappers % m) + bars
    print(count)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().split())
        chocolateFeast(n, c, m)