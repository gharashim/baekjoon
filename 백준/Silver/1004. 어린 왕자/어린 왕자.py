T = int(input())
answer = []
for _ in range(T):
    X = list(map(int, input().split()))
    n = int(input())
    R = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        da = ((R[i][0] - X[0]) ** 2 + (R[i][1] - X[1]) ** 2) ** 0.5
        db = ((R[i][0] - X[2]) ** 2 + (R[i][1] - X[3]) ** 2) ** 0.5
        r = float(R[i][2])

        if min(da, db) > r or max(da, db) < r:
            cnt += 0
        else:
            cnt += 1
        # print(da, db, r, cnt)
    answer.append(cnt)
[print(answer[i]) for i in range(T)]