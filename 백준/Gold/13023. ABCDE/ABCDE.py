import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 100)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i, depth):
    global tf
    visit[i] = 1

    if depth == 4:
        tf = True
        return
    
    for j in graph[i]:
        if visit[j] == 0:
            visit[j] = 1
            dfs(j, depth + 1)
            visit[j] = 0

answer = 0
for i in range(N):
    tf = False
    dfs(i, 0)
    visit[i] = 0

    if tf == True:
        answer = 1
        break

print(answer)