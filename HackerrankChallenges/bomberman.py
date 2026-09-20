def bomberMan(r, c, n, grid):
    if n == 1:
        return grid

    # all cells filled with bombs
    if n % 2 == 0:
        return ['O' * c for i in range(r)]

    # alternate states
    n //= 2
    for q in range((n+1) % 2 + 1):
        new_grid = [['O'] * c for i in range(r)]

        # func for detonation
        def setting(x, y):
            if 0 <= x < r and 0 <= y < c:
                new_grid[x][y] = '.'
        xi = [0, 0, 0, 1, -1]
        yi = [0, -1, 1, 0, 0]

        for x in range(r):
            for y in range(c):
                # check for bomb
                if grid[x][y] == 'O':
                    # detonate the cell by calling setting()
                    for i, j in zip(xi, yi):
                        setting(x+i, y+j)

        grid = new_grid
        return ["".join(x) for x in grid]


if __name__ == '__main__':
    r, c, n = map(int, input().split())
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    arr = "\n".join(bomberMan(r, c, n, grid))
    print(arr)