import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())

graph = [[ 0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, length):
    graph[x][y] = 1 # 해당 좌표 방문
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if graph[nx][ny] == 0:
                length = dfs(nx, ny, length + 1)
    return length

answer = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            answer.append(dfs(i, j, 1))

print(len(answer))
print(*sorted(answer))