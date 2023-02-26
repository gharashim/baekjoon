N, M = map(int, input().split())
pocket = [i+1 for i in range(N)]
num_ = [list(map(int, input().split())) for _ in range(M)]
for iter in range(M):
    i, j, k = num_[iter]
    pocket[i-1:j] = pocket[k-1:j] + pocket[i-1:k-1]
print(*pocket)