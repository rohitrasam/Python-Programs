def maximumPerimeterTriangle(sticks):
    sticks.sort()
    perimeters = {}

    for i in range(len(sticks)-1, 1, -1):
        if sticks[i] < sticks[i-1] +  sticks[i-2]:
            perimeters[sticks[i] + sticks[i-1] + sticks[i-2]] = [sticks[i], sticks[i-1], sticks[i-2]]
    
    if len(perimeters) == 0:
        return -1
    
    return sorted(perimeters.get(max(perimeters.keys())))


n = int(input())
sticks = list(map(int, input().split()))

result = maximumPerimeterTriangle(sticks)
print(result)