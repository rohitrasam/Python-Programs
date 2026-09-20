def lilysHomework(arr):
    def swap(srt_arr):
        org_arr = arr.copy()

        dict_arr = {}

        for i in range(len(arr)):
            dict_arr[arr[i]] = i

        swp = 0
        for i in range(len(org_arr)):
            if org_arr[i] != srt_arr[i]:
                swp += 1

                ind_swap = dict_arr[srt_arr[i]]
                dict_arr[org_arr[i]] = ind_swap
                org_arr[i], org_arr[ind_swap] = org_arr[ind_swap], org_arr[i]
            
        return swp

    return min(swap(sorted(arr)), swap(sorted(arr, reverse=True)))
            
            
if __name__ == '__main__':
    n = int(input())

    A = list(map(int, input().split()))

    result = lilysHomework(A)
    print(result)

    
    