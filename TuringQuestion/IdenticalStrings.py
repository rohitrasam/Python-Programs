# Two strings are identical if the have the same characters 
# for eg. "good" is identical to "god" as both have {"g", "o", "d"}"
# "python" and "yarn" however, are not
# Find such pairs of strings such tha 0 <= x < y <= str.length -1

def identical_strings(strs: list[str]) -> int:
    ...    

if __name__ == '__main__':

    strings = input().split()

    print(identical_strings(strings))