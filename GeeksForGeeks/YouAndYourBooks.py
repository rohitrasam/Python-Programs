
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, a):
        #code here
        total = 0
        max_ = 0
        for i in range(n):
            if a[i] <= k:
                total += a[i]
                max_ = max(max_, total)
            else:
                max_ = max(max_, total)
                total = 0

        return max_
            
        
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa
# } Driver Code Ends