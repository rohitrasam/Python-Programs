# You are required to complete this method
# You may use module's
class Solution:
    def max_val(self, arr, n):
        # code here
        max_val = -2131249124123123
        val = 0
        left = 0
        right = n-1

        while left < right:
            if arr[left] < arr[right]:
                val = arr[left] * (right-left)
                left += 1
            else:
                val = arr[right]*(right-left)
                right -= 1
            
            max_val = max(max_val, val)

        return max_val

#{ 
# Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().max_val(arr, n))
# } Driver Code Ends