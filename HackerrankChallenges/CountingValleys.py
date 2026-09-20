def countingValleys(n, s):
    valleys = 0
    unit = 0
    for i in s:
        if i == 'U':
            unit += 1
        elif i == 'D':
            unit -= 1
        if i == 'U' and unit == 0:
            valleys += 1

    print(valleys)


if __name__ == '__main__':
    n = int(input())
    s = input()

    countingValleys(n, s)