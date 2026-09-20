def geo_dist(n, p):
    return (1-p)**(n-1)*p


num, den = map(int, input().split())
n = int(input())
p = num / den
ans = sum([geo_dist(i, p) for i in range(1, n+1)])
print(round(ans, 3))
