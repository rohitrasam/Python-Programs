import numpy as np
r = c = 4


def minCost(cost, m, n):
    tc = np.array([[0 for x in range(c)] for x in range(r)])
    print(tc, '\n')
    tc[0, 0] = cost[0, 0]
    print(tc, '\n')

    for i in range(1, m+1):
        tc[i, 0] = tc[i-1, 0] + cost[i, 0]
        print(tc, '\n')

    for j in range(1, n+1):
        tc[0, j] = tc[0, j-1] + cost[0, j]
        print(tc, '\n')

    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i, j] = min(tc[i-1, j-1], tc[i-1, j], tc[i, j-1]) + cost[i, j]
            print(tc, '\n')

    return tc[m, n]


cost = np.array([[1, 4, 3, 1], [5, 3, 8, 2], [7, 1, 9, 3], [8, 6, 3, 2]])
print(cost, '\n')
print(minCost(cost, 3, 3))
