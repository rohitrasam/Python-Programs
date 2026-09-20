from collections import Counter

def makingAnagrams(str1: str, str2: str):
    str1 = Counter(str1)
    str2 = Counter(str2)
    s1 = str1 - str2
    s2 = str2 - str1

    return sum(s1.values()) + sum(s2.values())
            

if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)
    print(result)