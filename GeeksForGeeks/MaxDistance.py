
def maxDistance(s: str, x: str) -> int:

    if len(s) == 1:
        return -1

    left = -1
    right = -1
    for start in range(len(s)):
        last = len(s) - start - 1
        if left == -1 and s[start] == x:
            left = start
        if right == -1 and s[last] == x:
            right = last

    if left == right:
        return -1

    visited = set()

    for idx in range(left+1, right):
        if s[idx] != " " and s[idx] != x:
            visited.add(s[idx])
            
    return len(visited)



if __name__ == '__main__':
    case1 = "i love gfg", "g"
    case2 = "haryana", "a"
    case3 = "geeksforgeeks", "z"
    case4 = "c", "c"
    case5 = "uzgwbb hatf b ckv h pl rcd e um vnac p rx xj azvtfyy i l e a eye v", "a"
    case6 = "l qy w w ndhe txv g a y af u ug il yy f sa c", "x"
    print(maxDistance(*case1))
    print(maxDistance(*case2))
    print(maxDistance(*case3))
    print(maxDistance(*case4))
    print(maxDistance(*case5))
    print(maxDistance(*case6))