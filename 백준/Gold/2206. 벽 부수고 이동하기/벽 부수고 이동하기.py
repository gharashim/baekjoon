from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    line = input()
    line_list = []
    for i in range(M):
        line_list.append(int(line[i]))
    graph.append(line_list)

q = deque()
q.append([0, 0, 0])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1

while q:
    w, y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if graph[ny][nx] == 0 and visited[w][ny][nx] == 0:
                visited[w][ny][nx] = visited[w][y][x] + 1
                q.append([w, ny, nx])

            elif graph[ny][nx] == 1 and w == 0:
                visited[w + 1][ny][nx] = visited[w][y][x] + 1
                q.append([w + 1, ny, nx])

answer = -1
if visited[w][N - 1][M - 1] > 0:
    answer = visited[w][N - 1][M - 1]

print(answer)