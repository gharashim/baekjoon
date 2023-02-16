N, M = map(int, input().split())
num_ = [input() for _ in range(N)]

def count_diff(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    return cnt

min_ = 99999999999
for i in range(M-7):
    for j in range(N-7):
        board = ''
        for k in range(j,j+8):
            board += num_[k][i:i+8]
        count = min(
            count_diff(board, ''.join(['WB' * 4 + 'BW' * 4] * 4)),
            count_diff(board, ''.join(['BW' * 4 + 'WB' * 4] * 4))
            )
        if min_ > count:
            min_ = count
print(min_)