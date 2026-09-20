def organizingContainers(container):
    row = [0] * n
    col = [0] * n

    for x in range(n):
        for y in range(n):
            row[x] += container[x][y]
            col[x] += container[y][x]

    if sorted(row) == sorted(col):
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    q = int(input())

    for i in range(q):
        n = int(input())
        container = []

        for _ in range(n):
            container.append(list(map(int, input().split())))

        organizingContainers(container)
