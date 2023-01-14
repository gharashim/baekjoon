num_list = [int(input()) for _ in range(9)]
max = -1
for i in range(9):
    if num_list[i] > max:
        max = num_list[i]
        idx = i + 1
print(max)
print(idx)