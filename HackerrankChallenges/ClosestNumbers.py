def sort_array(arr):

    if len(arr) > 1:
        left_arr = sort_array(arr[:len(arr)//2])
        right_arr = sort_array(arr[len(arr)//2:])


        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
    return arr

def closestNumbers(arr):
    arr = sort_array(arr)
    smallest = abs(arr[-1] - arr[-2])
    output = []

    for i in range(len(arr)):
        if abs(arr[i] - arr[i-1]) <= smallest:
            smallest = arr[i] - arr[i-1]

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) == smallest:
            output.append(arr[i-1])    
            output.append(arr[i])    

    return output




if __name__ == '__main__':
    
    n = int(input())

    A = list(map(int, input().split()))
    result = closestNumbers(A)
    print(result)