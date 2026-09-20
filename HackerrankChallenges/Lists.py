if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        s = input()
        if s == "insert":
            i, num = int(input())
            list.insert(i, num)
        elif s == "print":
            print(list)
        elif s == "remove":
            num = int(input())
            list.remove(num)
        elif s == 'append':
            num = int(input())
            list.append(num)
        elif s == 'sort':
            list.sort()
        elif s == 'pop':
            list.pop()
        elif s == 'reverse':
            list. reverse()
