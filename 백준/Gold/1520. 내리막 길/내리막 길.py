import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(y, x):
    if (y == M - 1) and (x == N - 1):
        return 1

    if visit[y][x] != -1:
        return visit[y][x]
    
    visit[y][x] = 0

    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N \
            and graph[ny][nx] < graph[y][x]:
            cnt += dfs(ny, nx)

    visit[y][x] = cnt
    return visit[y][x]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

visit = [[-1 for _ in range(N)] for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0))