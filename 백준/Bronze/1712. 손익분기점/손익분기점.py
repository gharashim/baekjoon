A, B, C = map(int, input().split())
n = -1
if C > B:
    n = int(A / (C - B)) + 1
print(n)