N, M = map(int, input().split())
graph = [ [ ] for _ in range(N + 1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b] += [a]

stack = []
result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    visit = [False for _ in range(N + 1)]
    stack.append(i)
    visit[i] = True

    # dfs 영역 -> dfs 알고리즘을 재귀 없이 구현
    while stack:
        result[i] += 1

        for j in graph[stack.pop()]:
            if not visit[j]:
                stack.append(j)
                visit[j] = True

for i in range(1, N + 1):
    if result[i] == max(result):
        print(i, end = ' ')