def binarySearch():
    pass


def exponential(length: int, array, item_search: any):
    """
    Function to search for a given item in a sorted array.

    :param item_search: Item to search for in the array.
    :param length: The length of the array that is passed to the function.
    :param array: An array of `int` .
    """

    if arr[0] == item_search:
        return 0

    i = 1
    while i < length and arr[i] <= item_search:
        i *= 2


if __name__ == '__main__':
    arr = sorted(list(map(int, input().split())))
    n = len(arr)
    x = int(input("Enter the item to search for: "))
    result = exponential(n, arr, x)

    if result == -1:
        print("{} is not found".format(x))
    else:
        print("{} found at {}".format(x, result))