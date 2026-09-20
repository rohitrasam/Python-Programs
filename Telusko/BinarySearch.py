def search(arr, n):
    low = 0
    u = len(arr)-1

    while low <= u:
        mid = (low + u)//2

        if arr[mid] == n:
            return True, mid+1
        elif arr[mid] < n:
            low = mid+1
        else:
            u = mid-1

    return False


arr = sorted(list(map(int, input().split())))
n = int(input('Search value: '))
print(arr)

result = search(arr, n)

if result[0]:
    print("Found at:", result[1])
else:
    print('Not found')
