def findDigits(n):
    count = 0
    num = n
    while n > 0:
        rem = n % 10
        if rem == 0:
            n //= 10
            continue
        if num % rem == 0:
            count += 1
        n //= 10

    return count


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        print(findDigits(n))
