N, K = map(int, input().split())
k = 0
x = 0
while(k < K):
    x += 1
    if x <= N:
        if N % x == 0:
            k += 1
    else:
        x = 0
        break
print(x)