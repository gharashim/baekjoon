import sys
sys.setrecursionlimit(100000)

def cut(i):
    mothers[i] = -2
    for j in range(N):
        if i == mothers[j]:
            cut(j)

N = int(input())
mothers = list(map(int, input().split()))
d = int(input())

cut(d)
leaf = 0

for i in range(N):
    if (mothers[i] != -2) & (i not in mothers):
        leaf += 1

print(leaf)