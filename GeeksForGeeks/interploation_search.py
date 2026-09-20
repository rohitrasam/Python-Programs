def interpolation_Search(arr, x, n):
    lo = 0
    hi = n - 1
    while lo <= hi and arr[lo] <= x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1

        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1


arr = list(map(int, input().split()))
x = int(input())

n = len(arr)

index = interpolation_Search(arr, x, n)
if index != -1:
    print("Number {} found at position {}".format(x, index+1))
else:
    print("Element not found")