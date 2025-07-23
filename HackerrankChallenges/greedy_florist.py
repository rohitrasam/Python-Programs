def getMinimumCost(k, costs):

    if k == len(costs):
        return sum(costs)

    costs.sort(reverse=True)
    total_cost = 0
    n = len(costs)
    prev_cost = 1
    for i in range(n):
        total_cost += costs[i] * prev_cost
        if (i + 1) % k == 0:
            prev_cost += 1
    
    return total_cost


n, k = map(int, input().split())
c = list(map(int, input().split()))

result = getMinimumCost(k, c)
print(result)