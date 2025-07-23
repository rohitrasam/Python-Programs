def birthday(s, d, m, n):
    count = 0
    for i in range(0, n - m + 1):
        if sum(s[i:m+i]) == d:
            count += 1

    print(count)


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    d, m = map(int, input().split())

    birthday(s, d, m, n)
