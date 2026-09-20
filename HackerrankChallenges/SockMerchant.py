def sockMerchant(n, ar):
    ar.sort()
    pairs = {}
    i = 0
    while i < n:
        pairs[ar[i]] = ar.count(ar[i]) // 2
        i += ar.count(ar[i])
    count = 0
    for value in pairs.values():
        if value != 0:
            count += value
    print(count)

    # def sockMerchant(n, ar):
    #     ar.sort()
    #     pairs = {}
    #     for i in range(n):
    #         pairs[ar[i]] = ar.count(ar[i]) // 2
    #     count = 0
    #     for value in pairs.values():
    #         if value != 0:
    #             count += value
    #     print(count)
    #

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))

    sockMerchant(n, ar)