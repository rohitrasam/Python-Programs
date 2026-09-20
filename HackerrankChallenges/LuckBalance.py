def luck_balance(k, contests):
    contests.sort(key=lambda x: x[0], reverse=True)
    total_luck = 0

    for contest in contests:
        if contest[1] == 0:
            total_luck += contest[0]
        elif k != 0 and contest[1] == 1:
            total_luck += contest[0]
            k -= 1
        else:
            total_luck -= contest[0]
    
    return total_luck


n, k = map(int, input().split())
contest = []

for _ in range(n):
    contest.append(list(map(int, input().split())))


result = luck_balance(k, contest)
print(result)