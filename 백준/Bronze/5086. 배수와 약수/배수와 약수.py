num_ = []
while(1):
    num_.append(list(map(int, input().split())))
    if num_[-1] == [0, 0]: break


for i in range(len(num_)-1):
    if num_[i][1] % num_[i][0] == 0: print('factor')
    elif num_[i][0] % num_[i][1] == 0: print('multiple')
    else: print('neither')