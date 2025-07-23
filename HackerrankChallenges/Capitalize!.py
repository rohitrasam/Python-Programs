def solve(s: str) -> str:
    # if s.isnumeric():
    #     return s
    # new_s = s.split(' ')
    # arr = []
    # for item in new_s:
    #     arr.append(item[0].upper() + item[1:])
    # ans = ' '.join(arr)
    # return ans
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
