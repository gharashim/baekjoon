import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    if stamp[y][x] != 0:
        return stamp[y][x]
    
    stamp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < dim_n) & (0 <= nx < dim_n):
            if bamboo[y][x] < bamboo[ny][nx]:
                stamp[y][x] = max(stamp[y][x], dfs(ny, nx) + 1)
    
    return stamp[y][x]

dim_n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(dim_n)]

dx = [1, 0, -1, 0]
dy = [0 ,1, 0, -1]

cnt = 0
stamp = [[0 for _ in range(dim_n)] for _ in range(dim_n)]

result = 0

for y in range(dim_n):
    for x in range(dim_n):
        result = max(result, dfs(y, x))
print(result)