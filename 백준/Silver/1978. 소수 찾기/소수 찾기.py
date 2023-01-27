N = int(input())
num = list(map(int, input().split()))

for num_ in num:
    n = 2
    if num_ > 2:
        while(1):
            if num_ % n == 0:
                N -= 1
                break
            if num_ // n == 1:
                break
            n += 1
    elif num_ == 1: N -= 1
print(N)