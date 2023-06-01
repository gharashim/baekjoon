import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

cheeze = []

for _ in range(N):
    cheeze.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(y, x):

    if cheeze[y][x] == 0:
        cheeze[y][x] = -1
    else:
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < N) and (0 <= nx < M):
            dfs(ny, nx)

answer = 0
while(1):

    if max([max(c) for c in cheeze]) == 0:
        break

    dfs(0,0)

    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if cheeze[y][x] == 1:
                melt = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if cheeze[ny][nx] == -1:
                        melt += 1
                
                if melt >= 2:
                    cheeze[y][x] = 0

    for y in range(N):
        for x in range(M):  
            if cheeze[y][x] < 0:
                cheeze[y][x] = 0
    
    answer += 1

print(answer)