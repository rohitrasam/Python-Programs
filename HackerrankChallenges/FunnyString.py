def funnyString(string: str):
    # Write your code here
    
    diff = [abs(ord(a)-ord(b)) for a, b in zip(string, string[1:])]
    return 'Funny' if diff == diff[::-1] else 'Not Funny'
    
    # stringRev = string[::-1]
    # vals1 = []
    # vals2 = []

    # for i in range(1, len(string)):
    #     vals1.append(abs(ord(string[i]) - ord(string[i-1])))
    #     vals2.append(abs(ord(stringRev[i]) - ord(stringRev[i-1])))

    # return 'Funny' if vals1 == vals2 else 'Not Funny'    

    
if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input()

        result = funnyString(s)

        print(result)
