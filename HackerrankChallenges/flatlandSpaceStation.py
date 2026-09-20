def SpaceStation(n, c):
    answer = 0
    c.sort()

    for i in range(1, len(c)):
        dist = c[i] - c[i-1]
        dist2 = dist // 2
        answer = max(answer, dist2)

    corner1 = c[0]
    corner2 = n-1 - c[-1]
    answer = max(answer, corner1, corner2)

    print(answer)


if __name__ == '__main__':
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    SpaceStation(n, c)
