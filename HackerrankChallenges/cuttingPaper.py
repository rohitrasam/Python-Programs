def solve(n, m):
    return (m * n) - 1


nm = input().split()
n = int(nm[0])
m = int(nm[1])
result = solve(n, m)
print(result)
