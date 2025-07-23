class Solution:	
    def remove_duplicate(self, A: list, N):
        # code here
        for i in range(N-1):
            if A[i] == A[i+1]:
                A.pop(i)
                A.insert(i, 0)
        while 0 in A:
            A.remove(0)

        return len(A) 


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends