import sys
sys.setrecursionlimit(100000)

N = int(input())

num = []
for _ in range(N - 1):
    num.append(list(map(int, input().split())))

graph   = [[] for _ in range(N + 1)]
visit   = [[] for _ in range(N + 1)]
parent  = [[] for _ in range(N + 1)]

for i, j in num:    
    graph[i] += [j]
    graph[j] += [i]

def dfs(i):
    visit[i] = 1

    for ii in graph[i]:
        if not visit[ii]:
            parent[ii] = i
            dfs(ii)

dfs(1)

for i in range(2, N + 1):
    print(parent[i])