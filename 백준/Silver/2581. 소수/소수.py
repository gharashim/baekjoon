prime_num = []

M = int(input())
N = int(input())

while(1):
    if M > 1:
        prime = True
        n = 2
        if M > 2:
            while(1):
                if M % n == 0:
                    prime = False
                    break
                if M // n == 1:
                    break
                n += 1
        if M == N + 1 : break
        if prime == True: prime_num.append(M)
    M += 1

if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))