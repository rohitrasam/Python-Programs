def howManyGames(p, d, m, s):
    total = s
    games = 0
    sum1 = 0
    while sum1 <= total:
        sum1 += p
        s -= p
        p -= d
        games += 1
        if p <= m:
            p = m
    print(games-1)


if __name__ == '__main__':
    p, d, m, s = input().split()

    howManyGames(int(p), int(d), int(m), int(s))