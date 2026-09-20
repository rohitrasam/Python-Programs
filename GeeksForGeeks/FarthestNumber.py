from typing import List


class Solution:
    def farNumber(self, N : int, A : List[int]) -> List[int]:
        # code here
        pass

#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.farNumber(N, A)
        
        IntArray().Print(res)
        

# } Driver Code Ends