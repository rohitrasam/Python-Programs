ratio = (list(map(float, input().split())))
inspection = int(input())
p = ratio[0] / ratio[1]

ans = ((1-p) ** (inspection-1)) * p

print('{}'.format(round(ans, 3)))
