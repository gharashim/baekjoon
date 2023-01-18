T = int(input())
input_ = [list(input().split()) for _ in range(T)]

answer = ''
for j in range(T):
    for i in range(len(input_[j][1])):
        answer += input_[j][1][i]*int(input_[j][0])
    print(answer)
    answer =''