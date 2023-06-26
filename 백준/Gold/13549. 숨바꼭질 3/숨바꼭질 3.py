from collections import deque

graph = [ -1 for _ in range(100001) ]
visited = [ -1 for _ in range(100001) ]

N, M = map(int, input().split())

# print(graph[0: M + 1])

q = deque()
q.append(N)
visited[N] = 0
graph[N] = 0

while q:
    x = q.popleft()
    if x == M:
        print(graph[x])
        break
    dx = [x - 1, x + 1, x * 2]
    
    if ( 0 <= dx[0]) and visited[dx[0]] == -1:
        visited[dx[0]] = visited[x] + 1
        graph[dx[0]] = graph[x] + 1
        q.append(dx[0])

    if (dx[2] < 100001 ) and visited[dx[2]] == -1:
        visited[dx[2]] = visited[x]
        graph[dx[2]] = graph[x]
        q.appendleft(dx[2])

    if (dx[1] < 100001 ) and visited[dx[1]] == -1:
        visited[dx[1]] = visited[x] + 1
        graph[dx[1]] = graph[x] + 1
        q.append(dx[1])
