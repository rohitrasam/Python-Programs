def beautifulDays(i, j, k):
    count = 0
    days = [x for x in range(i, j+1)]
    for y in days:
        copy = y
        rev = 0
        while y > 0:
            lsb = y % 10
            rev *= 10
            rev += lsb
            y //= 10
        absolute = abs(copy - rev)
        if absolute % k == 0:
            count += 1
    print(count)


if __name__ == '__main__':

    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])

    beautifulDays(i, j, k)