num_ = list(map(int, input().split()))

gcd = min(num_)
lcm = max(num_)

while(1):
    a = num_[0] // gcd
    b = num_[1] // gcd
    if (num_[0] % gcd == 0) & (num_[1] % gcd == 0): break
    else: gcd -= 1

lcm = gcd * a * b

print(gcd)
print(lcm)