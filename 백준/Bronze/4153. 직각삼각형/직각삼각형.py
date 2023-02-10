num_input = []
while(1):
    num_ = sorted(list(map(int, input().split())))
    if num_[0] == 0: break
    num_input.append(num_)

for i in range(len(num_input)):
    if num_input[i][2] ** 2 == num_input[i][0] ** 2 + num_input[i][1] ** 2:
        print('right')
    else:
        print('wrong')