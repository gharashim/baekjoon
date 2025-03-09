n = int(input())

dp = [0] * (10**6 + 1)

def one(n):
    if n < 2 : return 0
    if dp[n]: return dp[n]
    for i in range(2, n+1):
        dp[i] = one(i-1) + 1
        if i % 3 == 0: dp[i] = min(dp[i], one(i//3) + 1)
        if i % 2 == 0: dp[i] = min(dp[i], one(i//2) + 1)
    return dp[n]

print(one(n))