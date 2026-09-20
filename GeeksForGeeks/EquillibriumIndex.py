# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    s = sum(a)
    left_sum = 0
    for i in range(0, n):
        s-=a[i]
        if left_sum == s:
            return i
        left_sum += a[i]
        
        
    return -1


    



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(findEquilibrium(arr,n))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends