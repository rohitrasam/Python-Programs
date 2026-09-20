def countSort(arr):
    # Write your code here
    arr = list(map(lambda data: [int(data[0]), data[1]], arr))
    max_int = max(arr, key=lambda x: x[0])
    helper = []
    for _ in range(max_int[0]+1):
        helper.append([])
    
    for ind in range(len(arr)):
        if ind < len(arr) // 2:
            helper[arr[ind][0]].append('-')
        else:
            helper[arr[ind][0]].append(arr[ind][1])

    result = " ".join([j for i in helper for j in i])
    print(result)


if __name__ == '__main__':
    n = int(input())
    A = []


    for _ in range(n):
        A.append(input().split())
        
        

    A = list(map(lambda data: [int(data[0]), data[1]], A))
    countSort(A)

