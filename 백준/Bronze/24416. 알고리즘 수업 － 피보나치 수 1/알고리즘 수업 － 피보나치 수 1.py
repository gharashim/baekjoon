N = int(input())
global na, nb
na = 0
nb = 0

def fib(n):
    global na
    if n == 1 or n == 2:
        na += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global nb
    f = []
    f.append(1)
    f.append(1)

    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
        nb += 1
    return f[n-1]

fib(N)
fibonacci(N)
print(na, nb)