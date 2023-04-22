N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if S[i][j] == 1:
            house.append([i, j])
        elif S[i][j] == 2:
            chicken.append([i, j])

def distance(list_a, list_b):
    return max(list_a[0], list_b[0]) - min(list_a[0], list_b[0]) +\
            max(list_a[1], list_b[1]) - min(list_a[1], list_b[1])

survived_chick = []
d_list = []

def dfs(iter):
    d = []
    if len(survived_chick) == M:
        for h in house:
            min_ = 99999999999999999
            for s in survived_chick:
                min_ = min(min_, distance(h, s))
            d.append(min_)
        d_list.append(sum(d))
        d = []
        return
    
    for i in range(iter, len(chicken)):
        survived_chick.append(chicken[i])
        dfs(i + 1)
        survived_chick.pop()

dfs(0)
print(min(d_list))