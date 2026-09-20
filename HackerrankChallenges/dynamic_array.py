def dynamicArray(n: int, queries: list[list[int]]):
    arr = []
    lastAnswer = 0
    for _ in range(n):
        arr.append([])

    ans = []

    for row in queries:
        if row[0] == 1:
            idx = (row[1] ^ lastAnswer) % n
            arr[idx].append(row[2])
        else:
            idx = (row[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][row[2] % len(arr[idx])]
            ans.append(lastAnswer)
    
    return ans


if __name__ == '__main__':
    n, q = map(int, input().split())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    print(dynamicArray(n, queries))



