from collections import deque

M, N, H = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(H)]

for z in range(H):
    for y in range(N):
        graph[z][y] = list(map(int, input().split()))

dx = [1, 0 ,-1, 0, 0, 0]
dy = [0, 1 ,0, -1, 0, 0]
dz = [0, 0 ,0, 0, 1, -1]

queue = deque()

for x in range(M):
        for y in range(N):
            for z in range(H):
                if graph[z][y][x] == 1:
                    queue.append([z, y, x])

while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < M) and (0 <= ny < N) and (0 <= nz < H):
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nz, ny, nx])

answer = []
for z in range(H):
    ans = 0
    for y in range(N):
        for j in graph[z][y]:
            if j == 0:
                print(-1)
                exit()

        ans = max(ans, max(graph[z][y]))
    answer.append(ans)
print(max(answer) - 1)