N, K = map(int, input().split())
W = [0]
V = [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
    
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < W[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]] + V[i])

print(dp[N][K])