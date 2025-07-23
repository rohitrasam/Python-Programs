def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        print(10000)
    elif m1 > m2 and y1 == y2:
        print(500 * (abs(m2 - m1)))
    elif d1 > d2 and m1 == m2 and y1 == y2:
        print(15 * (abs(d2 - d1)))
    else:
        print(0)


if __name__ == '__main__':
    d1, m1, y1 = input().split()
    d2, m2, y2 = input().split()

    libraryFine(int(d1), int(m1), int(y1), int(d2), int(m2), int(y2))
