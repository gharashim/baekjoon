N, M = map(int, input().split())

graph = [ [ 0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플루이드 - 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):

            if i != j:
                if graph[i][k] != 0 and graph[k][j] != 0:
                    if graph[i][j] == 0:
                        graph[i][j] = graph[i][k] + graph[k][j]
                    else:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_ = 99999999999
answer = -1
for i in range(1, N + 1):
    if min_ > sum(graph[i]):
        min_ = sum(graph[i])
        answer = i

print(answer)