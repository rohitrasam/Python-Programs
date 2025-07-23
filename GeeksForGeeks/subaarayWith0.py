# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

# Example 1:

# Input:
# 5
# 4 2 -3 1 6

# Output: 
# Yes

# Explanation: 
# 2, -3, 1 is the subarray 
# with sum 0.
# Example 2:

# Input:
# 5
# 4 2 0 1 6

# Output: 
# Yes

# Explanation: 
# 0 is one of the element 
# in the array so there exist a 
# subarray with sum 0.

#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        for i in arr:
            if i == 0:
                return "Yes"

        total = 0
        h = {}
        for i in range(n):
            total += arr[i]
            if total == 0 or h.get(total) == 1:
                return True
            else:
                h[total] = 1

        return False


        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends