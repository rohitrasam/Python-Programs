def checkPermutation(value, position, ans):
    return abs(value - position) +1 != ans

def absolutePermutation(n, k):
    pos = list(range(1, n+1))
    
    if k == 0:
        return pos
    elif n % 2 == 1:
        return [-1]
    
    for i in range(0, n-k):
        if pos[i] == pos[i+k] -k:
            pos[i], pos[i+k] = pos[i+k], pos[i]
        elif checkPermutation(pos[i], i, k):
            return [-1]

    for i in range(n-k, n):
        if checkPermutation(pos[i], i, k):
            return [-1]
    
    return pos



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        result = absolutePermutation(n, k)
        print(result)