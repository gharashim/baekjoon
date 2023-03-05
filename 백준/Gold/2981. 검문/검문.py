def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    gcd_val = numbers[0]
    for i in range(1, len(numbers)):
        gcd_val = gcd(gcd_val, numbers[i])
    return gcd_val

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

T = int(input())
num_ = sorted([int(input()) for _ in range(T)])
interval = []
for i in range(1, len(num_)):
    interval.append(num_[i] - num_[i - 1])
print(*get_divisors(gcd_list(interval))[1:])