def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.{}'.format(year)
    elif 1700 <= year <= 1917:
        if year % 4 == 0:
            return '12.09.{}'.format(year)
        else:
            return '13.09.{}'.format(year)
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return '12.09.{}'.format(year)
    else:
        return '13.09.{}'.format(year)


if __name__ == '__main__':
    year = int(input())

    print(dayOfProgrammer(year))
