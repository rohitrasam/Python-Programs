
# #User function Template for python3

# class Solution:
#     #Function to find triplets with zero sum.    
#     def findTriplets(self, arr, n):
#         #code here

#         for i in range(n-1):
#             s = set()
#             for j in range(i+1, n):
#                 x = -(arr[i] + arr[j])
#                 if x in s:
#                     return True
#                 s.add(arr[j])
            
            
#         return False
            
# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# if __name__=='__main__':
#     t = int(input())
#     for i in range(t):
#         n=int(input())
#         a=list(map(int,input().strip().split()))
#         if(Solution().findTriplets(a,n)):
#             print(1)
#         else:
#             print(0)
# # } Driver Code Ends


# def towerOfHanoi(n: int):
#     if n == 1:
#         return 1

#     return 2*towerOfHanoi(n-1) +1

# if __name__ == '__main__':
#     rings = int(input())

#     print(towerOfHanoi(rings))



# import time
# def hanoi(num):
#     if num <= 1:
#         return 1
#     else:
#         return 2*hanoi(num-1) + 1

# start = time.time()
# print(hanoi(64))
# end = time.time()
# print(f"TIME = {end-start}")

