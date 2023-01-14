input_ = []
while(1):
    num = list(map(int, input().split()))
    if num[0] == 0 & num[1] == 0: break
    input_.append(num)
[print(sum(input_[i])) for i in range(len(input_))]