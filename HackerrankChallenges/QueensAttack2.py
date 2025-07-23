def queensAttack(n, k, rq, cq, obstacles):
    total = 0
    obs = {}
    for i, j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j: 1}

    def limit(x, y):
        if 1 <= x <= n and 1 <= y <= n:
            return True
        else:
            return False

    def check(x, y, xi, yi):
        count = 0
        x += xi
        y += yi
        while limit(x, y) and obs.get(x, {}).get(y, 0) == 0:
            count += 1
            x += xi
            y += yi
        return count

    r = [0, 0, -1, 1, -1, 1, -1, 1]
    c = [1, -1, 0, 0, -1, 1, 1, -1]

    for i, j in zip(r, c):
        total += check(rq, cq, i, j)

    print(total)


if __name__ == '__main__':
    n, k = map(int, input().split())
    rq, cq = map(int, input().split())

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().split())))

    queensAttack(n, k, rq, cq, obstacles)





    # board = []
    # for i in range(n, 0, -1):
    #     a = []
    #     for j in range(1, n+1):
    #         if i == rq and j == cq:
    #             a.append('Q')
    #             # print('Q', end=' ')
    #         else:
    #             m = 0
    #             for o in range(len(obstacles)):
    #                 for m in range(1):
    #                     if i == obstacles[o][m] and j == obstacles[o][m+1]:
    #                         a.append('X')
    #                         # print('X', end=' ')
    #                 if i == obstacles[o][m] and j == obstacles[o][m + 1]:
    #                     break
    #             else:
    #                 a.append(0)
    #                 # print(0, end=' ')
    #     board.append(a)
    # print(np.array(board))

