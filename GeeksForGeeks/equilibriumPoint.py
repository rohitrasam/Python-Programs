# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Note: Retun the index of Equilibrium point. (1-based index)

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 3 
# Explanation:  
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2). 
 

# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 1
# Explanation:
# Since its the only element hence
# its the only equilibrium point.



# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        # if N == 1:
        #     return N

        total = sum(A)
        left = 0
        for i in range(N):
            if total - left - A[i] == left:
                return i + 1
            else:
                left += A[i]
        
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends