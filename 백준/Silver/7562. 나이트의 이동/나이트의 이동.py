from collections import deque

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

N = int(input())

for _ in range(N):
    I = int(input())
    start   = list(map(int, input().split()))
    end     = list(map(int, input().split()))

    graph = [[0 for _ in range(I)] for _ in range(I)]
    graph[start[0]][start[1]] = 1

    q = deque()
    q.append(start)

    while q:
        y, x = q.popleft()

        if [y, x] == end:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < I) and (0 <= ny < I):
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = graph[y][x] + 1
                        q.append([ny, nx])
    print(graph[end[0]][end[1]] - 1)