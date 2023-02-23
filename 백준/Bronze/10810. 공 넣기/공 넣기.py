N, M = map(int, input().split())
pocket = [0] * N
num_ = [list(map(int, input().split())) for _ in range(M)]
for m in range(M):
    i, j, k = num_[m]
    pocket[i-1:j] = [k] * (j - i + 1)
print(*pocket)