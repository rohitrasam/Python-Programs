def chessboardGame(row, col):
    return 'Second' if 0 < row%4 < 3 and 0 < col%4 < 3 else 'First' 

if __name__ == '__main__':

    t = int(input().split())

    for _ in range(t):
        x, y = list(map(int, input().split()))


        result = chessboardGame(x, y)