def jumpingOnTheClouds(c):
    jumpCount = 0
    i = 0
    while True:
        if i == len(c) - 2:
            jumpCount += 1
            i += 2
            break
        if c[i+2] == 1:
            jumpCount += 1
            i += 1
        else:
            jumpCount += 1
            i += 2
    print(jumpCount)


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().split()))

    jumpingOnTheClouds(c)
