def serviceLane(width, cases):
    result = []
    for i, j in cases:
        result.append(min(width[i:j+1]))

    print(*result, sep='\n')


if __name__ == '__main__':
    n, t = map(int, input().split())
    width = list(map(int, input().split()))

    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().split())))

    serviceLane(width, cases)