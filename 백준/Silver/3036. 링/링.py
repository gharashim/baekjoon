def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

N = int(input())
num_ = list(map(int, input().split()))
for i in range(1, N):
    gcd_ = gcd(num_[0], num_[i])
    print('{}/{}'.format(num_[0]//gcd_, num_[i]//gcd_))