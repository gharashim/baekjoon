def w(a, b, c):
    global dp # global 변수 dp에 값들을 저장
    if a <= 0 or b <= 0 or c <= 0: return 1
    elif a > 20 or b > 20 or c > 20: return w(20, 20, 20)
    # dp 값들은 0으로 초기화 해두었는데 0이 아니라면 이미 계산 완료되었으므로 그대로 가져다 쓴다.
    elif dp[a][b][c] != 0: return dp[a][b][c] 
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
# dp 0부터 21까지 0으로 초기화
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while(1):
    num_ = list(map(int, input().split()))
    if num_[0] == -1 and num_[1] == -1 and num_[2] == -1:
        break
    print('w({}, {}, {}) = {}'.format(*num_, w(*num_)))