def missingItem(x):
    for i in range(len(x)-1):
        if abs(x[i] - x[i+1]) != 2:
            return x[i] + 2


if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))

    print(missingItem(x))
