N = int(input())
L = int(input())

Link = [list(map(int, input().split())) for _ in range(L)]
graph = [[] for _ in range(N + 1)]

for i,j in Link:
    graph[i] += [j]
    graph[j] += [i]

visit = [0] * (N + 1)

def dfs(i):
    visit[i]=1
    for j in graph[i]:
        if visit[j]==0:
            dfs(j)
dfs(1)
print(sum(visit)-1)