num = [int(input()) for _ in range(10)]
print(len(set([num[i]%42 for i in range(len(num))])))