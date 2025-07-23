def jumpingOnClouds(c, k):
    e = 100
    for i in range(0, len(c), k):
        e -= 1
        position = c[(i+k) % len(c)]
        if position == 1:
            e -= 2
    print(e)


if __name__ == '__main__':
    n, k = input().split()
    c = list(map(int, input().split()))
    jumpingOnClouds(c, int(k))
