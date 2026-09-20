def iceCreamParlor(m, arr):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                print(i+1, j+1)
                break


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().split()))

        iceCreamParlor(m, arr)
