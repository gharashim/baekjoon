import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = []
visit = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if visit[x][y] == 1:
        return False
    
    visit[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if graph[x][y] == graph[nx][ny]:
            dfs(nx, ny)
            
    return True

cnt = 0
answer = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1

answer.append(cnt)

cnt = 0
visit = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
            
answer.append(cnt)      
print(*answer)