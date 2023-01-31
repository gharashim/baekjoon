A = [list(map(int, input().split())) for _ in range(9)]

max_ = -1

for i in range(9):
    for j in range(9):
        if A[i][j] > max_:
            max_ = A[i][j]
            idx = i
            jdx = j

print(max_)
print(idx + 1, jdx + 1)