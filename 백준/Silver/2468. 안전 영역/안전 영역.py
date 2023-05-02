import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
    global binary
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if binary[x][y] == 1:
        binary[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

answer = []
for h in range(min(min(graph)), max(max(graph)) + 1):
    
    binary = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= h:
                binary[i][j] = 1
                
    count = 0

    for i in range(N):
        for j in range(N):
            if dfs(i,j) == True:
                count += 1
    
    answer.append(count)

print(max(answer))