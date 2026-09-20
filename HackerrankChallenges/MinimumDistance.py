def minimumDistance(arr):
    dist = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                dist.append(abs(i - j))

    if len(dist) == 0:
        print(-1)
    else:
        print(min(dist))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    minimumDistance(a)
