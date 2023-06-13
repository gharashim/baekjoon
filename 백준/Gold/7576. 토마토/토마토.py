from collections import deque

M, N = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

dx = [1, 0 ,-1, 0]
dy = [0, 1 ,0, -1]

queue = deque()

for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                queue.append([y, x])

while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0 <= ny < N):
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

answer = 0
for i in range(N):
    for j in graph[i]:
        if j == 0:
            print(-1)
            exit()

    answer = max(answer, max(graph[i]))
print(answer - 1)