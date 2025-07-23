from random import randrange


class Solution:
    def solve(self, N, K, A):
        maps = {}
        for i in range(0, N):
            if A[i] not in maps.keys():
                maps[A[i]] = 1
            else:
                maps[A[i]] += 1
                

        i = 0
        while True:
            if i not in maps.keys():
                K -= 1
            if K == 0:
                return i
            i += 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    sol = Solution()
    print(sol.solve(n,k,a))
# } Driver Code Ends