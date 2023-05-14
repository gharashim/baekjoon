import sys
sys.setrecursionlimit(10**4)

def dfs(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                if ice_berg[ny][nx] > 0:
                    dfs(ny, nx)

N, M = map(int, input().split())

ice_berg = []

for _ in range(N):
    ice_berg.append(list(map(int, input().split())))
visit = [[ 0 for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

year = 0
answer = 0

while True:
    cnt = 0

    for y in range(N):
        for x in range(M):
            if ice_berg[y][x] > 0 and visit[y][x] == 0:
                dfs(y, x)
                cnt += 1
    
    # print(ice_berg)

    if (cnt > 1) or max([max(i) for i in ice_berg]) <= 0:
        break
    
    year += 1

    for y in range(N):
        for x in range(M):
            if ice_berg[y][x] > 0 and visit[y][x] == 1:
                visit[y][x] = 0
                ice = ice_berg[y][x]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if ny >= 0 and ny < N and nx >= 0 and nx < M:
                        if ice_berg[ny][nx] <= 0 and visit[ny][nx] == 1:
                            ice -= 1
                            if ice <= 0:
                                ice = 0
                                break
                ice_berg[y][x] = ice

if cnt <= 1:
    answer = 0
else:
    answer = year
print(answer)