def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def lcm(a, b):
    gcd_value = gcd(a, b)  # 최대공약수 계산
    return (a * b) // gcd_value  # 최소공배수 계산

T = int(input())
[print(lcm(*list(map(int, input().split())))) for _ in range(T)]