# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# In case of multiple subarrays, return the subarray which comes first on moving from left to right.

 
# Example 1:

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.

#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        #Write your code here
        # start = 0 
        # end = 0
        # for i in range(n-1):
        #     total = arr[i]
        #     for j in range(i+1, n):
        #         total += arr[j]
        #         if total == s:
        #             start = i + 1
        #             end = j + 1
        #             break
        #     if total == s:
        #         break
        
        # return [-1] if start == 0 and end == 0 else [start, end]

        start = 0
        end = 0
        total = arr[0]
        if total == s:
            return [1, 1]
        
        if s == 0:
            return [-1]

        while end < n-1:
            if total + arr[end+1] <= s:
                total += arr[end+1]
                end += 1
            else:
                total -= arr[start]
                start += 1
            
            if total == s:
                return start+1, end+1
        
        return [-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends