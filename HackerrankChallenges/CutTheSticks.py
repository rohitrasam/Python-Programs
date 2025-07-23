def cutTheSticks(arr):
    while arr is not None:
        if len(arr) == 0:
            break
        print(len(arr))
        minLength = min(arr)
        for i in range(len(arr)):
            arr[i] -= minLength
        while 0 in arr:
            arr.pop()


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    cutTheSticks(arr)
