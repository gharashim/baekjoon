L, C = map(int, input().split())
char = sorted(list(input().split()))

answer = []

def dfs(iter):
    if len(answer) == L:
        if (len(set(['a', 'e', 'i', 'o', 'u']) & set(answer)) >= 1)\
            & (len(set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']) \
            & set(answer)) >= 2):
            print(''.join(answer))
        return
    
    for i in range(iter, C):
        answer.append((char[i]))
        dfs(i + 1)
        answer.pop()
        
dfs(0)