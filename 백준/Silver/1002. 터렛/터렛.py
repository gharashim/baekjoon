T = int(input())
case_ = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    d = ((case_[i][0] - case_[i][3]) ** 2 + (case_[i][1] - case_[i][4]) ** 2 ) ** 0.5
    r1 = case_[i][2]
    r2 = case_[i][5]

    if d > 0:
        if max(r1, r2) <= d:
            if (r1 + r2) > d: answer = 2
            elif (r1 + r2) == d: answer = 1
            else: answer = 0

        elif max(r1, r2) > d:
            if abs(r1 - r2) < d: answer = 2
            elif abs(r1 - r2) == d: answer = 1
            else: answer = 0

    else:
        if r1 == r2: answer = -1
        else: answer = 0

    print(answer)