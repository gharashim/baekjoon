def bubble_sort(L, R):
    if L > R: return R, L
    else: return L, R

def sweep(a):
    for i in range(len(a)-1):
        a[i], a[i+1] = bubble_sort(a[i], a[i+1])
    return a

def check_rank(a):
    output = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]: output = False
    return output

a = [int(input()) for _ in range(5)]

while(1):
    if check_rank(a) == False: a = sweep(a)
    else: break

print(int(sum(a) / 5))
print(a[2])