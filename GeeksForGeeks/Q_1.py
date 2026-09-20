from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        temp = []
        for item in arr:
            if len(temp) == 0:
                temp.append(item)
            else:    
                if temp[-1] >=0 and item >= 0:
                    temp.append(item)
                elif temp[-1] < 0 and item < 0:
                    temp.append(item)
                else:
                    temp.pop() 
                
        return temp
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends


# string = 'Abc_123_xyz_20_10'

# string = string.split('_')

# total = 0

# for item in string:
#     if item.isnumeric():
#         total += int(item)

# print(total)