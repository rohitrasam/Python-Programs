def balancedSums(arr):
    n = len(arr)
    s = sum(arr)
    l = 0
    for x, i in zip(arr, range(n)):
        # r = s - x - l
        if s - x - l - l == 0:
            return True
        l += x
    return False


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        arr = list(map(int, input().split()))

        print(["NO", "YES"][balancedSums(arr)])
