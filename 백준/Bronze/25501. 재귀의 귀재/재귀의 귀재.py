def recursion(s, l, r, k):
    if l >= r:
        return 1, k
    elif s[l] != s[r]:
        return 0, k
    else:
        k += 1
        return recursion(s, l+1, r-1, k)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

N = int(input())
[print(*list(isPalindrome(input()))) for _ in range(N)]