import sys
T = int(sys.stdin.readline().strip())
input_ = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
[print('Case #{}: {} + {} = {}'.format(i+1, input_[i][0], input_[i][1], sum(input_[i]))) for i in range(T)]