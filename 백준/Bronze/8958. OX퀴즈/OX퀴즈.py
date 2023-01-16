N = int(input())
ox = [input() for _ in range(N)]


cnt = 0
score = []

for j in range(N):
    for i in range(len(ox[j])):
        if ox[j][i] == 'O':
            cnt += 1
        else :
            cnt = 0
        score.append(cnt)
    print(sum(score))
    cnt = 0
    score = []