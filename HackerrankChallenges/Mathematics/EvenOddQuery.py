from typing import List


def solve(arr: List[int], queries: List[int]) -> List[str]:
    
    lst = []
    for i,j in queries:
        if arr[i-1]%2:
            lst.append('Odd')
        elif i != j and arr[i] == 0:
            lst.append('Odd')
        else:
            lst.append('Even')
    return lst

if __name__ == '__main__':


    a = [3, 2, 7]
    q = [1, 2], [2, 3]

    print(solve(a, q))

