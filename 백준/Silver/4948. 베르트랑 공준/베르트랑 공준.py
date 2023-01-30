input_ = []
while(1):
    int_ = int(input())
    if int_ == 0: break
    input_.append(int_)

def prime_list(M, N):
    tf = [True] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if tf[i] == True:
            for j in range(i + i, N+1, i):
                tf[j] = False
    return [i for i in range(N+1) if (tf[i] == True) & (i > M ) & (i != 1)]

[print(len(prime_list(input_[i], 2 * input_[i]))) for i in range(len(input_))]