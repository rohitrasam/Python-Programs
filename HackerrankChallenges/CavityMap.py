def cavityMap(grid):

    grid = [list(x) for x in grid]

    for j in range(1, n-1):
        for k in range(1, n-1):
            if grid[j][k] > grid[j-1][k] and grid[j][k] > grid[j+1][k] and grid[j][k] > grid[j][k-1] and grid[j][k] > grid[j][k+1]:
                grid[j][k] = 'X'
    grid = ["".join(x) for x in grid]
    print(*grid, sep='\n')


if __name__ == '__main__':
    n = int(input())

    grid = []
    for i in range(n):
        grid.append(input())

    cavityMap(grid)
