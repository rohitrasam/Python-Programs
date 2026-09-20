from typing import List

class Solution:
    def toggle(self, n : int, arr : List[int]) -> int:
        # code here
        ans = 0
        ones_front = [0]

        for el in arr:
            if el == 1:
                ones_front.append(ones_front[-1]+1)
            else:
                ones_front.append(0)
            
        ans = max(ans, max(ones_front))
        ones_back = [0]

        for el in arr[::-1]:
            if el == 1:
                ones_back.append(ones_back[-1] + 1)
            else:
                ones_back.append(0)

        ones_back = ones_back[::-1]
        temp = 0

        for i in range(n):
            el = arr[i]
            if el == 0:
                temp += 1
                curr = i - temp + 1
                left = ones_front[curr]
                right = ones_back[i+1]
                ans = max(ans, left+right+temp)
            else:
                temp = 0
        
        return ans



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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.toggle(n, arr)
        
        print(res)
        