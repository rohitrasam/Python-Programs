def palindromeIndex(string):
    
    if string == string[::-1]:
        return -1
    
    for i in range(len(string) // 2 + len(string)%2):
        if string[i] != string[len(string) - i - 1]:
            temp = string[:i] + string[i+1:]
            if temp == temp[::-1]:
                return i
            else:
                return len(string) - i - 1
    return -1

if __name__ == '__main__':

    q = int(input())

    for _ in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)