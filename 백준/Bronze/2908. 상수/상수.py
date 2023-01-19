num = input().split()
num1 = int(''.join([num[0][len(num[0])-i-1] for i in range(len(num[0]))]))
num2 = int(''.join([num[1][len(num[1])-i-1] for i in range(len(num[1]))]))
print(max(num1, num2))