
""" Youtube solution"""
def activityNotifications(expenditure, d):
    # Write your code here

    count = {}
    
    def get_median(idx):
        s = 0
        for i in range(201):
            freq = 0
            if i in count:
                freq = count[i]
            s += freq
            if s >= idx:
                return i
    notify = 0
    
    for i in range(len(expenditure)):
        val = expenditure[i]
        
        if i >= d:
            med = get_median(d//2 + d%2)
            
            if d%2 == 0:
                if val >= med + get_median(d//2 + 1):
                    notify += 1
            else:
                if val >= med*2:
                    notify += 1
        
        # add current value to dict slinding window
        if val not in count:
            count[val] = 1
        else:
            count[val] += 1
        
        # remove element out of sliding window
        if i >= d:
            prev = expenditure[i-d]
            count[prev] -= 1


if __name__ == '__main__':
    n, d = map(int, input().split())

    exp = list(map(int, input().split()))


    result = activityNotifications(exp, d)
    print(result)