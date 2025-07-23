from time import time
class Solution:
    def removeDuplicates(self, arr: list):
        # code here

        count = [0] * 100
        result = []
        t0 = time()
        for i in arr:
            if count[i] == 0:
                count[i] = 1
                result.append(i)
        t1 = time()
        print(t1-t0)


        return result


        """My Solution"""
        # arr = arr[::-1]
        # i = 0
        # t0 =time()
        # while i < len(arr):
        #     if arr.count(arr[i]) > 1:
        #         arr.remove(arr[i])
        #     else:
        #         i += 1
        # t1 = time()
        # print(t1-t0)
        
        
        # return arr[::-1]

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().removeDuplicates(arr)
        for i in range(len(res)):
            print(res[i], end=" ")


# } Driver Code Ends