# Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

# Example 1:

# Input:
# N = 4
# a[] = {0,3,1,2}
# Output: -1
# Explanation: N=4 and all elements from 0
# to (N-1 = 3) are present in the given
# array. Therefore output is -1.
# Example 2:

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 2 3 
# Explanation: 2 and 3 occur more than once
# in the given array.

class Solution:
    def duplicates(self, arr, n): 
    	# code here

        dups = {}
        for j in arr:
            dups[j] = 0

        for i in arr:
            dups[i] += 1

        ans = []

        for key in dups.keys():
            if dups[key] > 1:
                ans.append(key)

        return [-1] if len(ans) == 0 else ans 
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends