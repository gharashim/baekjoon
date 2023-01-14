N, X = map(int, input().split())
num = list(map(int, input().split()))
answer = 0
answer = [answer + num[i] for i in range(N) if num[i] < X]
print(*answer)