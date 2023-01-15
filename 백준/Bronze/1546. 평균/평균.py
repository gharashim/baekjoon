N = int(input())
score = list(map(int, input().split()))
max = -1
for i in range(len(score)):
    if score[i] > max:
        max = score[i]
score = [score[i] / max * 100 for i in range(len(score))]
print(sum(score)/len(score))