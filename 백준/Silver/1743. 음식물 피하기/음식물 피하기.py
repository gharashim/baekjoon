import sys
sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x):
    global cnt
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    
    if visit[y][x] == 1:
        return
    visit[y][x] = 1

    if graph[y][x] == 0:
        return

    if graph[y][x] == 1:
        cnt += 1
        graph[y][x] = 0
        # visit[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(ny, nx)
            
answer = - 999
for y in range(N):
    for x in range(M):
        visit = [[0 for _ in range(M)] for _ in range(N)]
        cnt = 0
        dfs(y, x)
        if answer < cnt:
            answer = cnt
print(answer)