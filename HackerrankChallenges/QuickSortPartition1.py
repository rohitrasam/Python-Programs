def quickSort(arr):

    pivot = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            ele = arr.pop(i)
            arr.insert(0, ele)
    return arr


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    result = quickSort(A)

