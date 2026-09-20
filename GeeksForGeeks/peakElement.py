# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


# Example 1:

# Input: 
# N = 3
# arr[] = {1,2,3}
# Possible Answer: 2
# Generated Output: 1
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.
# If 2 is returned then the generated output will be 1 else 0.
# Example 2:

# Input:
# N = 2
# arr[] = {3,4}
# Possible Answer: 1
# Output: 1
# Explanation: 4 (at index 1) is the 
# peak element as it is greater than 
# its only neighbour element 3.
# If 1 is returned then the generated output will be 1 else 0.


# your task is to complete this function
# function should return index to the any valid peak element
            
    
class Solution:   
    def peakElement(self,arr, n):
        # Code here

        # TC - O(n) 
        # for i in range(n):
        #     if i == 0 and arr[i] >= arr[i+1]:
        #         return i
        #     elif i == n-1 and arr[i] >= arr[i-1]:
        #         return i
        #     elif arr[i-1] <= arr[i] >= arr[i+1]:
        #         return i
        
        lo = 0
        hi = n - 1
        mid = (lo + hi) // 2

        while lo <= hi:
            if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == n-1 or arr[mid] >= arr[mid+1]):
                return mid
            elif mid > 0 and arr[mid-1] > arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1






#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
