# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Example 2:

# Input:
# N = 4, K = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.

#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        m = {}

        for i in range(n):
            if arr[i] in m.keys():
                m[arr[i]] += 1
            else:   
                m[arr[i]] = 1

        
        twice_count = 0

        for i in range(n):
            if k -arr[i] in m.keys():
                twice_count += m[k-arr[i]]

            if k - arr[i] == arr[i]:
                twice_count -= 1

        return twice_count // 2




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends