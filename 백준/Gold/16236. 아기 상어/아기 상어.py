import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bitefish(y, x, shark_size):
    
    visited = [ [0 for _ in range(N)] for _ in range(N)]
    distance = [ [0 for _ in range(N)] for _ in range(N)]
    q = deque()

    q.append([y, x])
    visited[y][x] = 1

    temp = []

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ( 0 <= nx < N ) and ( 0 <= ny < N ) and visited[ny][nx] == 0:
                if graph[ny][nx] <= shark_size:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[y][x] + 1

                    if graph[ny][nx] < shark_size and graph[ny][nx] != 0:
                        temp.append([ny, nx, distance[ny][nx]])
    
    # 거리가 가까운 물고기가 많다면,
    # 가장 위에 있는 물고기,
    # 그러한 물고기가 여러마리라면,
    # 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
result = 0
size = 2

for j in range(N):
    for i in range(N):
        if graph[j][i] == 9:
            y = j
            x = i

while True:
    shark = bitefish(y, x, size)

    if len(shark) == 0:
        break

    ny, nx, dist = shark.pop()

    result += dist
    graph[y][x] = 0
    graph[ny][nx] = 0

    y, x = ny, nx
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

print(result)