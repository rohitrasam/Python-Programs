def permutationEquation(p):
    return [(p.index(p.index(i)+1)+1) for i in range(1, max(p)+1)]


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))

    y = permutationEquation(p)
    for j in y:
        print(j)
