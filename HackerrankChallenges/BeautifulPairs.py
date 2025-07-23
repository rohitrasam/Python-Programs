from collections import Counter

def beautifulPairs(a, b):
    pairs = 0
    ac = Counter(a)
    bc = Counter(b)

    for val in ac:
        if val in bc:
            pairs += min(ac[val], bc[val])
        
    if pairs == len(a):
        return pairs - 1
    else:
        return pairs + 1



if __name__ == '__main__':

    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = beautifulPairs(A, B)