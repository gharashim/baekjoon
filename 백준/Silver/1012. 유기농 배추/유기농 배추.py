import sys
sys.setrecursionlimit(10**6)

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = []

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
    

for _ in range(T):
    M, N, K = map(int, input().split())
    baechu = [list(map(int, input().split())) for _ in range(K)]
    
    graph = [[0 for _ in range(M)] for _ in range(N)]
    
    for x, y in baechu:
        graph[y][x] = 1
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                count += 1
    print(count)