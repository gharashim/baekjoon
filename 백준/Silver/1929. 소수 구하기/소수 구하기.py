M, N = map(int, input().split())

def prime_list(M, N):
    tf = [True] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if tf[i] == True:
            for j in range(i + i, N+1, i):
                tf[j] = False
    return [i for i in range(N+1) if (tf[i] == True) & (i >= M) & (i != 1)]
prime_num = prime_list(M, N)
[print(prime_num[i]) for i in range(len(prime_num))]