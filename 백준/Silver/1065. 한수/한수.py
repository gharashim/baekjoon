def hansu(N):
    N = str(N)
    if      int(N) < 100: return 1
    elif    int(N[1]) == 0.5 * (int(N[0]) + int(N[2])): return 1
    else: return 0

N = input()
sum_ = 0

for i in range(int(N)):
    sum_ += hansu(i+1)
print(sum_)