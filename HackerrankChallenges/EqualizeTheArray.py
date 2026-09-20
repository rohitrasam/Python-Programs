def equalizeArray(arr):
    dic = {}
    for i in arr:
        dic[arr.count(i)] = i
    most = max(dic.keys())
    ele = dic[most]
    c = 0
    for i in arr:
        if i != ele:
            c += 1
    print(c)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    equalizeArray(arr)
