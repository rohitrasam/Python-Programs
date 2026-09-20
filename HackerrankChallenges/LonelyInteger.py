from collections import Counter

def lonelyInteger(arr: list[int]):
    # counter = Counter(arr)
    # ans = list(filter(lambda x: x[1] == 1, counter.items()))
    # return ans[0][0]
    
    result = 0
    for i in arr:
        result ^= i
    return result

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().split()))

    result = lonelyInteger(a)

    print(result)