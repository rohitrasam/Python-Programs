def minimumNumber(num: int, string: str) -> int:

    special_characters = "!@#$%^&*()-+"
    count = 0
    if not any(i.isdigit() for i in string):
        count += 1
    if not any(i.isupper() for i in string):
        count += 1
    if not any(i.islower() for i in string):
        count += 1
    if not any(i in special_characters for i in string):
        count += 1

    return max(count, 6-num)


if __name__ == '__main__':
    n = int(input())
    password = input()
    print(minimumNumber(n, password))
