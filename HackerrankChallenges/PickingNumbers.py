def pickingNumbers(a):
    a.sort()
    p = []
    for i in range(len(a)-1):
        p1 = []
        for j in range(i+1, len(a)):
            if abs(a[i] - a[j]) == 0 or abs(a[i] - a[j]) == 1:
                if a[j] and a[i] not in p1:
                    p1.append(a[i])
                    p1.append(a[j])
                else:
                    p1.append(a[j])
        if len(p1) > 0:
            p.append(len(p1))
    print(max(p))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    pickingNumbers(a)
