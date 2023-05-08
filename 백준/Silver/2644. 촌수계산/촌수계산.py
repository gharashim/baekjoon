import sys
sys.setrecursionlimit(10000)

n = int(input())
a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

answer = -999
result = -1

def dfs(x, y, cnt):
    global result
    if x == y:
        result = cnt
        return

    visit[x] = 1
    for j in graph[x]:
        if visit[j] == 0:
            visit[j] = 1
            cnt += 1
            dfs(j, y, cnt)
            cnt -= 1


dfs(a,b,0)
print(result)