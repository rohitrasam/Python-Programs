#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        # code here
        pass
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = []
        for _ in range(E):
            a,b = map(int, input().split())
            adj.append([a,b])
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends