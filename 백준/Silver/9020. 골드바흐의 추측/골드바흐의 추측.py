T = int(input())
n = [int(input()) for _ in range(T)]

def find_prime(N):
    tf = [True] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if tf[i] == True:
            for j in range(i + i, N + 1, i):
                tf[j] = False
    return [i for i in range(2, N+1) if (tf[i] == True)]

for N in n:
    prime_list = find_prime(N)
    answer = N // 2
    while(1):
        if answer in prime_list:
            if N - answer in prime_list:
                print(answer, N - answer)
                break
            else: answer -= 1
        else: answer -= 1