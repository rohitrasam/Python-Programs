from math import inf


def minimumAbsoluteDifference(arr):
    arr.sort()
    min1 = inf
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min1:
            min1 = dif
    print(min1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    minimumAbsoluteDifference(arr)