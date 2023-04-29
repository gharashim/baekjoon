import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

num = []
for _ in range(M):
    num.append(list(map(int, input().split())))

graph = [[] for _ in range(N + 1)]

for i, j in num:    
    graph[i] += [j]
    graph[j] += [i]
    
visit = [0 for _ in range(N + 1)]

cnt = 0

def dfs(i):
    global cnt
    
    if visit[i] == 1:
        return False

    visit[i] = 1
    for j in graph[i]:
        if visit[j] == 0:
            visit[j] = 1
            dfs(j)
        else:
            return False
    return True
            
for i in range(1, N + 1):
    if dfs(i) == True:
        cnt += 1

print(cnt)