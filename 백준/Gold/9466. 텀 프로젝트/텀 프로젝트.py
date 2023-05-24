import sys
sys.setrecursionlimit(100000)

def dfs(i):
    global team
    visit[i] = 1
    tree.append(i)

    if visit[student[i]] == 1:
        if student[i] in tree:
            team += tree[tree.index(student[i]):]
    else:
        dfs(student[i])

T = int(input())

for _ in range(T):
    n = int(input())
    student = [-1] + list(map(int, input().split()))
    visit = [0 for _ in range(n + 1)]
    team = []

    for i in range(1, n + 1):
        if visit[i] == 0:
            tree = []
            dfs(i)

    print(n - len(team))