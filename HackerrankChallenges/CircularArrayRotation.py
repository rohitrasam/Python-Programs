def circularArrayRotation(a, k, queries):

    for i in range(k):
        ele = a[len(a)-1]
        a.insert(0, ele)
        a.pop()

    for j in queries:
        print(a[j])


if __name__ == '__main__':

    n, k, q = input().split()
    a = list(map(int, input().split()))
    queries = []
    for _ in range(int(q)):
        queries.append(int(input()))

    circularArrayRotation(a, int(k), queries)
