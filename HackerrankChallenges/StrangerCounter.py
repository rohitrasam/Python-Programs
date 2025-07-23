def strangeCounter(n):
    time = 3
    while True:
        n -= time
        if n <= 0:
            n += time
            return time - n + 1

        time *= 2


if __name__ == '__main__':
    n = int(input())

    print(strangeCounter(n))