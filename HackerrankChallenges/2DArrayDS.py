def hourglass(a):
    max1 = -99
    for i in range(1, 5):
        for j in range(1, 5):
            sum1 = a[i][j] + a[i-1][j-1] + a[i-1][j] + a[i-1][j+1] + a[i+1][j+1] + a[i+1][j] + a[i+1][j-1]
            if sum1 > max1:
                max1 = sum1
    print(max1)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().split())))

    hourglass(arr)
