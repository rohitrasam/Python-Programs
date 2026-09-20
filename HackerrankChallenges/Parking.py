from locale import currency


def solve (N, Current: list[int], Desired: list[int]):
    # Write your code here
    if Current == Desired:
        return 0

    moves = 0
    i = 0
    j = 0
    
    while i < N-1:
        while j < N-1:
            if Desired[i] == Current[j]:
                i += 1
                j += 1
            else:
                idx = Desired.index(Current[j])
                if Current[idx] != Current[idx + 1]  and abs(idx - j) == 1 and Desired[idx-1] == 0:
                    vehicle = Current.pop(j)
                    Current.insert(idx, vehicle)
                    moves += 1
                    i += 1
                    j += 1 
                

T = int(input())
for _ in range(T):
    N = int(input())
    Current = list(map(int, input().split()))
    Desired = list(map(int, input().split()))

    out_ = solve(N, Current, Desired)
    print (out_)