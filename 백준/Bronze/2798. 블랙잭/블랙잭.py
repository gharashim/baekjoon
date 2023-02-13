N, M = map(int, input().split())
card = list(map(int, input().split()))

max_ = -1
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_ = sum([card[i], card[j], card[k]])
            if sum_ <= M:
                if max_ < sum_:
                    max_ = sum_
print(max_)