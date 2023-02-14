N = int(input())
for num_ in range(N):
    answer = sum([int(i) for i in str(num_)]) + num_
    if answer == N:
        break
    num_ = 0
print(num_)