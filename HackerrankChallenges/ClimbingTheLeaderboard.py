def climbingLeaderBoard(s, a):
    """My solution(runtime error)"""
    # i = 0
    # while i < len(alice):
    #     s.append(a[i])
    #     ranks = set(s)
    #     scores2 = list(ranks)
    #     scores2.sort(reverse=True)
    #     print(scores2.index(a[i])+1)
    #     s.remove(a[i])
    #     i += 1

    """Optimized solution #1"""
    s = sorted(list(set(s)), reverse=True)
    a.sort(reverse=True)
    j = 0
    l = len(s)
    result = []
    for i in range(len(a)):
        while j < l and a[i] < s[j]:
            j += 1
        result.append(j + 1)
    result.sort(reverse=True)

    for j in result:
        print(j)


if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().split()))

    alice_count = int(input())
    alice = list(map(int, input().split()))

    climbingLeaderBoard(scores, alice)
