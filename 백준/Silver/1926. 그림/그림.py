import sys
sys.setrecursionlimit(1000000)

def dfs(y, x):
    global area
    if visit[y][x] == 1:
        return False, area
    visit[y][x] = 1

    if pic[y][x] == 0:
        return False, area
    
    area += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < dim_y) & (0 <= nx < dim_x):
            if pic[y][x] == 1:
                # area += 1
                dfs(ny, nx)
    return True, area

dim_y, dim_x = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(dim_y)]

dx = [1, 0, -1, 0]
dy = [0 ,1, 0, -1]

visit = [ [0 for _ in range(dim_x)] for _ in range(dim_y)]

cnt = 0
area = 0
max_area = -999

for y in range(dim_y):
    for x in range(dim_x):
        yn, area = dfs(y, x)

        if yn == True:
            cnt += 1
        
        if max_area < area:
            max_area = area

        area = 0

print(cnt)
print(max_area)