N = [i+1 for i in range(30)]
target_list = [int(input()) for _ in range(28)]
[N.remove(target_list[i]) for i in range(len(target_list)) if target_list[i] in N]
print(*N)