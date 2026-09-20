
def hackerrankInString(string: str):
    # Write your code here
    original = 'hackerrank'

    cnt = 0
    ctr = 0
    for char in original:
        while ctr < len(string):
            if string[ctr] == char:
                cnt += 1
                ctr += 1
                break
            ctr += 1
        
    return 'YES' if cnt == 10 else "NO"

    

if __name__ == '__main__':

    n = int(input())


    for _ in range(n):
        s = input().strip()

        result = hackerrankInString(s)
        print(result )

