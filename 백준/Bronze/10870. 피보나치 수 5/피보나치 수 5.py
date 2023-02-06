def sum_(n):
    if n == 0: return 0
    elif n == 1: return 1
    return sum_(n-1) + sum_(n-2)
print(sum_(int(input())))