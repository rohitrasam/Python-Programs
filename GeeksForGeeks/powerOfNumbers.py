# Given a number and its reverse. Find that number raised to the power of its own reverse.
# Note: As answers can be very large, print the result modulo 109 + 7.

# Example 1:

# Input:
# N = 2
# Output: 4
# Explanation: The reverse of 2 is 2
# and after raising power of 2 by 2 
# we get 4 which gives remainder as 
# 4 by dividing 1000000007.
# Example 2:

# Input:
# N = 12
# Output: 864354781
# Explanation: The reverse of 12 is 21
# and 1221 , when divided by 1000000007 
# gives remainder as 864354781.

#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        def solve(N, R):

            if R == 0:
                return 1
            
            temp = solve(N, R//2) 
            sq = temp * temp
            if R % 2 == 0:
                return sq
            return N * sq % (10**9 + 7)

        
        return solve(N, R) % (10**9 + 7)

             
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends