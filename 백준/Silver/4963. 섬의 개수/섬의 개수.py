import sys
sys.setrecursionlimit(10000)

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

while True:
    w, h = map(int, input().split())
    
    if w == 0 & h == 0:
        break
    
    visit = [[0 for _ in range(w)] for _ in range(h)]
    graph = []

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0

    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                count += 1
    print(count)