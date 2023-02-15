N = int(input())
num_ = [list(map(int, input().split())) for _ in range(N)]
for i in range(0, N):
    cnt = 1
    for j in range(0, N):
        if j != i:
            if (num_[i][0] < num_[j][0]) & (num_[i][1] < num_[j][1]): cnt += 1
    print(cnt)