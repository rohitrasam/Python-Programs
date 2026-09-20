def countPrimeNumber(n):
    count = 0

    while n % 2 == 0:
        n = n / 2
        count += 1
    
    i = 3
    while i <= n**0.5:
        while n % i == 0:
            n /= i
            count += 1
        i += 2
    
    if n > 2:
        count += 1

    return count


def printKAlmostPrimes(k, n):
    #Code here
    i = 1
    num = 2

    while i <= n:
        if countPrimeNumber(num) == k:
            print(num, end='')
            print(" ", end='')

            i += 1
        num += 1   


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        k,n = list(map(int, input().strip().split()))
        printKAlmostPrimes(k, n)
        print('')
# Contributed by: Harshit sidhwa
# } Driver Code Ends