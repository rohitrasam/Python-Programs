def alternatingCharacters(string: str):
    # Write your code here

    # Solution 1
    deletions = 0
    for char1, char2 in zip(string, string[1:]):
        if char1 == char2:
            deletions += 1

    return deletions

    # Solution 2

    # ans = []
    # deletions = 0
    # for char in string:
    #     if len(ans) == 0:
    #         ans.append(char)
    #     else:
    #         if ans[-1] != char:
    #             ans.append(char)
    #         else: 
    #             deletions += 1
    # return deletions




if __name__ == '__main__':

    q = int(input())

    for _ in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)