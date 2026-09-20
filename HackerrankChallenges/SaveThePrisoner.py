def savePrisoner(n, m, s):
    return (m % n + s - 1) % n or n


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m, s = map(int, input().split())
        print(savePrisoner(n, m, s))