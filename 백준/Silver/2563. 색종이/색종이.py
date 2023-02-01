T = int(input())

cordi = [ list(map(int, input().split())) for _ in range(T) ]

def get_square(i,j):
    a = []
    i_init = i
    j_init = j
    for _ in range(10):
        for _ in range(10):
            a.append('{}.{}'.format(i,j))
            i += 1
        i = i_init
        j += 1
    j = j_init
    return a

S = []
for i in range(len(cordi)):
    S += get_square(*cordi[i])

print(len(set(S)))