N = int(input())
depth = N // 2
S = []

for _ in range(N):
    S.append(list(map(int, input().split())))

team = []
index_ = []
temp = []
sum_ = []

def dfs_S(jter, len_r):
    global temp
    if len(index_) == 2:
        temp.append(S[team[index_[0]]][team[index_[1]]] +\
             S[team[index_[1]]][team[index_[0]]])
        return
    for j in range(jter, len_r):
        index_.append(j)
        dfs_S(j + 1, len_r)
        index_.pop()


def dfs(iter):
    global temp
    if len(team) == depth:
        dfs_S(0, len(team))
        sum_.append(sum(temp))
        temp = []
        return
    for i in range(iter, N):
        team.append(i)
        dfs(i + 1)
        team.pop()

dfs(0)

answer = []
for i in range(len(sum_)//2):
    answer.append(max(sum_[i], sum_[len(sum_) - i - 1]) -\
          min(sum_[i], sum_[len(sum_) - i - 1]))

print(min(answer))