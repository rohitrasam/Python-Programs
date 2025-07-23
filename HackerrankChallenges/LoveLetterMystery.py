def theLoveLetterMystery(string: str):
    # Write your code here
    operations = 0
    revString = string[::-1]
    if string == revString:
        return operations

    for idx in range(len(string)//2):
        if string[idx] != revString[idx]:
            operations += abs(ord(revString[idx]) - ord(string[idx]))
    
    return operations

            



if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input().strip()

        result = theLoveLetterMystery(s)
        
        print(result)

