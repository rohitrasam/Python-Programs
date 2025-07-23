from numpy import array as ar, shape


def isSafe(maze, row, col):
    n = shape(maze)[0]-1
    if row <= n-1 and col <= n-1:
        return True
    return False


def solveMaze(maze, row, col, sol):
    n = shape(maze)[0]-1
    if row == n-1 and col == n-1:
        print(sol)
        return True
    if isSafe(maze, row, col) and maze[row, col] == 1:
        sol[row, col] = 1
    if solveMaze(maze, row, col+1, sol):
        return True
    elif solveMaze(maze, row+1, col, sol):
        return True
    else:
        sol[row, col] = 0
        return False


if __name__ == '__main__':
    maze = ar([[1, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1, 1]])
    sol = ar([[0 for i in range(4)] for j in range(4)])
    solveMaze(maze, 0, 0, sol)
