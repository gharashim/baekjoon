N = int(input())

i = 1
j = 1

while(1):
    # print(i,j)
    print(' ' * (N - i) + '*' * ( 2 * i - 1 ))
    if j < N:
        i += 1
        j += 1
    else:
        i -= 1
        j += 1
    if j > (2 * N - 1): break