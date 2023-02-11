cham_oi = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

A = -1
for i in range(len(arr)):
    if arr[i][1] > A:
        A = arr[i][1]
        idx = i

def get_lr(idx):
    r = idx + 1
    l = idx - 1
    if idx == 5:
        r = 0
    if idx == 0:
        l = 5
    return [l,r]

if arr[get_lr(idx)[0]][1] > arr[get_lr(idx)[1]][1]:
    jdx = get_lr(idx)[0]
    B = arr[jdx][1]
else:
    jdx = get_lr(idx)[1]
    B = arr[jdx][1]

b = abs(arr[get_lr(idx)[0]][1] - arr[get_lr(idx)[1]][1])
a = abs(arr[get_lr(jdx)[0]][1] - arr[get_lr(jdx)[1]][1])

print(cham_oi * (A * B - a * b))