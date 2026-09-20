nums = {"I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XIX": 19,
        "XXX": 30,
        "XL": 40,
        "XLIX": 49,
        "L": 50,
        "XC": 90,
        "C": 100
        }
t = int(input())
for _ in range(t):
    a, b = input().split(" ")
    a = nums.get(a)
    b = nums.get(b)
    ans = list(nums.values())
    index = ans.index(a - b)
    keys = list(nums.keys())
    print(keys[index])
