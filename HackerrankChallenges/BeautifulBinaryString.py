def beautifulBinaryString(binString: str):
    # Write your code here

    operations = 0 
    arr = list(binString)

    for idx in range(0, len(arr)):
        if arr[idx:idx+3] == ['0', '1', '0']:
            arr[idx+2] = '1'
            operations += 1 
    return operations

    # operations = 0
    
    # for idx in range(0, len(binString)):
    #     if binString[idx:idx+3] == '010':
    #         binString = binString[:idx+2] + '1' + binString[idx+3:]
    #         operations += 1
    # return operations



if __name__ == '__main__':
    n = int(input())

    b = input()

    result = beautifulBinaryString(b)
    print(result)
