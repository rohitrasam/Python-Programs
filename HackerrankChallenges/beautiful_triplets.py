def beautifulTriplets(d, arr):
    counter = 0
    for i in arr:
        if i + d in arr and i + (2*d) in arr:
            counter += 1

    # i = 0
    # for j in range(n-2):
    #     i = j
    #     ans = set()
    #     while i < n:
    #         if arr[i] + d in arr:
    #             ans.add(arr[i])
    #             ans.add(arr[i]+d)
    #             i = arr.index(arr[i] + d)
    #         else:
    #             break

    #         if len(ans) == 3:
    #             counter += 1
    #             break
    return counter
        



if __name__ == '__main__':

    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    result = beautifulTriplets(d, arr)
    print(result)




