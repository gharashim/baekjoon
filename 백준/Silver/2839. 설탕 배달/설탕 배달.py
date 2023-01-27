N = int(input())
n = N // 5
n_ = N % 5

while(1):
    if n_ % 3 != 0:
        n -= 1
        n_ = N - 5 * n
    else: break

if n >= 0:
    print( n + n_ // 3 )
else :
    print( n )