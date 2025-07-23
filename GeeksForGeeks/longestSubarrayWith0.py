# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.

#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here

        h = {}
        total = 0
        max_len = 0
        for i in range(n):
            total += arr[i]
           
            if arr[i] == 0 and max_len == 0:
                max_len = 1
            
            if total == 0:
                max_len = i + 1
            
            if total in h:
                max_len = max(max_len, i - h[total])
            else:
                h[total] = i

        return max_len
    

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends