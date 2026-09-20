def pageCount(n, p):
    front = p // 2
    if n % 2 == 0:
        back = (n - p + 1) // 2
    else:
        back = (n - p) // 2
    # if n % 2 == 0
    # if p % 2 == 0:
    #     if p == n or p == 1:
    #         turns = 0
    #     elif p > n // 2:
    #         turns = n - p - 1
    #     elif p <= n // 2:
    #         turns = p - 1
    #
    # else:
    #     if p == n or p == 1:
    #         turns = 0
    #     elif p > n // 2:
    #         turns = n - p - 2
    #     elif p <= n // 2:
    #         turns = p - 2

    print(min(front, back))


if __name__ == '__main__':
    n = int(input())
    p = int(input())

    pageCount(n, p)