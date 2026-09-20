def search(arr, n):
    for i in arr:
        if i == n:
            return True, arr.index(i)+1

        return False


arr = list(map(int, input().split()))
n = int(input('Search value: '))
if search(arr, n)[0]:
    print('Found at:', search(arr, n)[1])
else:
    print('Not found')
