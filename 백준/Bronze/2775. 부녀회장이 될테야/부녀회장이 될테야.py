T = int(input())
K = []
N = []
for _ in range(T):
    K.append(int(input()))
    N.append(int(input()))

for i in range(T):
    k = K[i]
    n = N[i]


    S = [x+1 for x in range(n)]
    S_ = S
    for _ in range(k):
        for i in range(n-1):
            S_[0] = 1
            S_[i+1] = S_[i] + S[i+1]
        S = S_

    print(S[n-1])