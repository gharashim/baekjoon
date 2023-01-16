C = int(input())
scores = [list(map(int, input().split())) for _ in range(C)]

for j in range(C):
    score = scores[j]
    mean = sum(score[1:score[0]+1])/(len(score)-1)
    for i in range(1,score[0]+1):
        if score[i] > mean : score[i] = 1
        else : score[i] = 0
    print('{:.3f}%'.format(sum(score[1:score[0]+1])/(len(score)-1)*100))
