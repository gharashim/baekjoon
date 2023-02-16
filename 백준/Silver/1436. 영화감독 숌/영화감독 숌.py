N = int(input())
first = 665
cnt = 0
while(1):
    first += 1
    if '666' in str(first): cnt += 1
    if cnt == N: break
print(first)