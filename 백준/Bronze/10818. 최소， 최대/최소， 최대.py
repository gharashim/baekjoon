N = int(input())
num = list(map(int, input().split()))
min = 10000001
max = -min
for i in range(len(num)):
    if num[i] < min: min = num[i]
    if num[i] > max: max = num[i]
print(min, max)