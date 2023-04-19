N, S = map(int, input().split())
nums = list(map(int,input().split()))
cnt = 0

def dfs(iter):
    global cnt
    if len(s) == depth:
        if sum(s) == S:
            cnt += 1
        return
    
    for i in range(iter, len(nums)):
        s.append(nums[i])
        dfs(i + 1)
        s.pop()
        
for depth in range(1, N + 1):
    s = []
    dfs(0)

print(cnt)