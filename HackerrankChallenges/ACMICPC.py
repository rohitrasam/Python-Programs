def acmTeam(topic):
    maxSub = 0
    count = 0

    for i in range(n-1):
        for j in range(i+1, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1

            if sub > maxSub:
                maxSub = sub
                count = 1
            elif sub == maxSub:
                count += 1

    return [maxSub, count]


if __name__ == '__main__':
    n, m = map(int, input().split())

    topic = []
    for _ in range(n):
        topics = input()
        topic.append(topics)

    result = acmTeam(topic)
    print('{}\n{}'.format(result[0], result[1]))
