import sys
sys.setrecursionlimit(100000)

def dfs(i, score): # 트리 탐색 및 점수 기록
    for j, k in graph[i]:
        if visit[j] < 0:
            visit[j] = score + k
            dfs(j, score + k)
            
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    numbers = list(map(int, input().split()))
    for i in range(1, len(numbers) - 1, 2):
        graph[numbers[0]].append([numbers[i], numbers[i + 1]])

length_of_graph = [len(i) for i in graph]
start = length_of_graph.index(max(length_of_graph))

visit = [-1 for _ in range(n + 1)]
# head로 부터 가중치 누적이 가장 큰 branch 탐색
visit[start] = 0
dfs(start, 0)
start = visit.index(max(visit))
# start branch? : head - start 간 가중치 누적이 가장 큰 node
# start node로 부터 다른 node까지는 무조건 head를 지나친다.

visit = [-1 for _ in range(n + 1)]
visit[start] = 0
dfs(start, 0) # start node로 부터 다른 node 까지의 가중치 누적 계산
print(max(visit)) # 최댓값을 출력