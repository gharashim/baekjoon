def reverse(list_):
    return [list_[-1 - i] for i in range(len(list_))]

N, M = map(int, input().split())
num_ = [list(map(int, input().split())) for _ in range(M)]
pocket = [i for i in range(1, N + 1)]

for i in range(M):
    pocket[num_[i][0] - 1 : num_[i][1]] = \
        reverse(pocket[num_[i][0] - 1 : num_[i][1]])

print(*pocket)