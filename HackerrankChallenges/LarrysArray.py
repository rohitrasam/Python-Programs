def larrysArray(arr: list[int]):

    i = 1
    while i < len(arr) +1:
        ind = i -1
        if arr[ind] != i:
            loc = arr.index(i)
            dist = loc - ind
            if dist == 1:
                if ind + 2 >= len(arr):
                    return "NO"
                ele = arr.pop(ind)
                arr.insert(loc+1, ele)
            elif dist % 2 == 0:
                ele = arr.pop(loc)
                arr.insert(ind, ele)
            elif dist % 2 == 1:
                if ind + 2 >= len(arr):
                    return "NO"
                ele = arr.pop(loc)
                arr.insert(ind + 1, ele)
                i -= 1
        
        i += 1
    else:
        return "YES"
    

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))

        result = larrysArray(A)
        print(result)