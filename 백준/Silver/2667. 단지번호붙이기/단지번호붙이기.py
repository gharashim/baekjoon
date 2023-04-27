n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return 1
    return 0


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == 1:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])