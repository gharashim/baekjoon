T = int(input())
input_ = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    H, W, N = input_[i]
    n = 1
    m = 0

    for _ in range(N):
        m += 1
        if m == H:
            n += 1
            m = 0

    if m == 0:
        m = H
        n -= 1

    re = str(m) + str(n)
    if n < 10: re = str(m) + '0' + str(n)

    print(re)