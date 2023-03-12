def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

num_ = [list(map(int, input().split())) for _ in range(2)]
lcm_ = lcm(num_[0][1], num_[1][1])
num2 = lcm_ // num_[0][1] * num_[0][0] + \
     lcm_ // num_[1][1] * num_[1][0], lcm_
gcd_ = gcd(*num2)
print(num2[0] // gcd_, num2[1] // gcd_)