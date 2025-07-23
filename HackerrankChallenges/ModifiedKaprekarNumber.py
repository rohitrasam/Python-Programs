def kaprekarNumber(p, q):
    result = []
    for i in range(p, q+1):
        sqr = str(i**2)
        digits = len(sqr)

        first = sqr[:digits//2]
        second = sqr[digits//2:]
        if i == 1:
            result.append(i)
        elif digits > 1 and (int(first) + int(second)) == i:
            result.append(i)

    if len(result) == 0:
        print("INVALID RANGE")
    else:
        print(*result)


if __name__ == '__main__':
    p = int(input())
    q = int(input())

    kaprekarNumber(p, q)
