def almostSorted(arr: list[int]):
    # Write your code here
    sortedArray = sorted(arr) 

    def is_sorted(arr1, arr2):
        if arr1 == arr2:
            return True

    left_idx = 0
    
    while left_idx < len(arr) and arr[left_idx]  == sortedArray[left_idx]:
        left_idx += 1
    
    right_idx = len(arr)-1

    while right_idx >= 0 and arr[right_idx] == sortedArray[right_idx]:
        right_idx -= 1

    arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]


    if is_sorted(arr, sortedArray):
        print(f'yes\nswap {left_idx+1} {right_idx+1}')
    else:
        arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
        sub_arr = arr[left_idx:right_idx+1]
        sub_arr.reverse()
        if is_sorted(sub_arr, sortedArray[left_idx:right_idx+1]):
            print(f'yes\nreverse {left_idx+1} {right_idx+1}')
        else:
            print('no')
        

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))

    almostSorted(arr)

