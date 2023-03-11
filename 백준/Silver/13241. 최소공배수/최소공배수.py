def gcd(a, b):
    # a와 b의 최대공약수를 구하는 함수
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    # a와 b의 최소공배수를 구하는 함수
    return (a * b) // gcd(a, b)

num_ = list(map(int, input().split()))
print(lcm(*num_))