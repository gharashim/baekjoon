N, M = map(int, input().split())

S1 = [list(map(int, input().split())) for _ in range(N)]
S2 = [list(map(int, input().split())) for _ in range(N)]

for j in range(N):
    for i in range(M):
        S1[j][i] = S1[j][i] + S2[j][i]
    print(*S1[j])