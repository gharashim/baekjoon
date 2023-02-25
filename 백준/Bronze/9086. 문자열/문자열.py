N = int(input())
char = [input() for _ in range(N)]
[print(char[i][0] + char[i][-1]) for i in range(N)]