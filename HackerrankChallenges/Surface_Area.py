def surfaceArea(A, H, W):
    # top and bottom
    area = 2 * H * W

    # checks the limit
    def check(X, Y, I, J):
        return A[X + I][Y + J] if 0 <= X + I < H and 0 <= Y + J < W else 0

    # remaining surfaces
    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]

    for x in range(H):
        for y in range(W):
            for i, j in zip(xi, yi):
                # gives area from adjacent cells
                area += max(0, A[x][y] - check(x, y, i, j))

    return area


if __name__ == '__main__':
    h, w = map(int, input().split())

    a = []

    for _ in range(h):
        a.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(a, h, w)
    print(result)
