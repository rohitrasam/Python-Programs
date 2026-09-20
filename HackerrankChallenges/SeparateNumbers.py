
def separateNumbers(number: str):
    # Write your code here
    if len(number) == 1:
        return ["NO"]
    else:
        for i in range(1, len(number) //2 + 1):
            genString = number[:i]
            prev = int(genString)

            while len(genString) < len(number):
                next_num = prev + 1
                genString += str(next_num)
                prev = next_num
            

            if genString == number:
                return "YES", number[:i]

        return ["NO"]
    



if __name__ == '__main__':

    q = int(input())

    for _ in range(q):
        number = input()

        print(*separateNumbers(number))
    