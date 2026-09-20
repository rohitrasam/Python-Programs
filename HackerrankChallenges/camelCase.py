def camel_case(string: str) -> int:
    counter = 1
    for letter in string:
        if letter.isupper():
            counter += 1
    return counter


if __name__ == '__main__':
    s = input()

    print(camel_case(s))
