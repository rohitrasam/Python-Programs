if __name__ == '__main__':
    n = int(input())

    unsorted = []
    for _ in range(n):
        item = input()
        unsorted.append(item)

    unsorted.sort(key=int)
    print('\n'.join(unsorted))
