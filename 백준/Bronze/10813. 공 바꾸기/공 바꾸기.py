def change(x, y):
    dummy = y
    y = x
    x = dummy
    return [x, y]

N, M = map(int, input().split())
num_ = [list(map(int, input().split())) for _ in range(M)]
pocket = [i for i in range(1, N + 1)]

for i in range(M):
    pocket[num_[i][0] - 1], pocket[num_[i][1] - 1] = \
        change(pocket[num_[i][0] - 1], pocket[num_[i][1] - 1])
        
print(*pocket)