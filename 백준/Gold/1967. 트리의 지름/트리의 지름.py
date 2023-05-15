import sys
sys.setrecursionlimit(100000)

def dfs(i, score): 
    for j, k in graph[i]:
        if visit[j] < 0:
            visit[j] = score + k
            dfs(j, score + k)
            
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(1, n):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visit = [-1 for _ in range(n + 1)]
visit[1] = 0
dfs(1, 0)
start = visit.index(max(visit))

visit = [-1 for _ in range(n + 1)]
visit[start] = 0
dfs(start, 0)
print(max(visit))