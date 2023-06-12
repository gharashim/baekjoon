from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, list(input())))

dx = [1, 0 ,-1, 0]
dy = [0, 1 ,0, -1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0 <= ny < N):
                if graph[ny][nx] == 0:
                    continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))

    return graph[N-1][M-1]

print(bfs(0, 0))