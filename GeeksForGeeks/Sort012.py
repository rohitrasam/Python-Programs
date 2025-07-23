# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
# Example 2:

# Input: 
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.


#User function Template for python3


class Solution:
    def sort012(self,arr,n):
        # code here
        ptr1 = itr = 0
        ptr2 = n - 1

        while itr <= ptr2:
            if arr[itr] == 0:
                arr[itr], arr[ptr1] = arr[ptr1], arr[itr]
                itr += 1
                ptr1 += 1
            elif arr[itr] == 2:
                arr[itr], arr[ptr2] = arr[ptr2], arr[itr]
                ptr2 -= 1
            else:
                itr += 1
        
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends