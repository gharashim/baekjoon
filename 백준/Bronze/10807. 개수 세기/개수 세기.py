N = int(input())
num = list(map(int, input().split()))
v = int(input())
answer = 0
answer = [answer + 1 for i in range(N) if num[i] == v]
print(sum(answer))