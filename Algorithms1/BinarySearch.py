def search(arr):
    item = int(input("Enter the item to search: "))
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    arr = sorted(list(map(int, input().split())))
    print('The sorted array is {}'.format(arr))

    print('The item is at index {}'.format(search(arr)+1))
