from collections import deque

N, K = map(int, input().split())
graph = [ 0 for _ in range(200000 + 1)]

q = deque()
q.append(N)

while q:
    x = q.popleft()

    if x == K:
        break

    for i in [x - 1, x + 1, 2 * x]:
        if (0 <= i < 100001) and not graph[i]:
            graph[i] = graph[x] + 1
            q.append(i)

print(graph[x])