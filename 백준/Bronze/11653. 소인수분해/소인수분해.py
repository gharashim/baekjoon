N = int(input())
n = 2
while(1):
    while(1):
        if N % n == 0:
            print(n)
            N = N / n
        else:
            break
    n += 1
    if N == 1: break