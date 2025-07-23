from collections import Counter

def anagram(string: str):

    if len(string) % 2 == 1:
        return -1

    a = string[:len(string)//2]
    b = string[len(string)//2:]

    changes = 0
    for char in a:
        if char not in b:
            changes += 1
        else:
            b = b.replace(char, '', 1)
    return changes


"""Solution 2"""

    # string = Counter(string[:len(string)//2]) - Counter(string[len(string)//2:])
    # return sum(string.values())



if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        result = anagram(s)
        print(result)