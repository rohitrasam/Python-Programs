
def marcsCakewalk(calories: list[int]):
    calories.sort(reverse=True)
    total_cal = 0
    for index in range(len(calories)):
        total_cal += 2 ** index * calories[index]
    
    print(total_cal)





if __name__ == '__main__':
    n = int(input())
    cal = list(map(int, input().split()))
    marcsCakewalk(cal)
