
def fibonacci(N):
    fib=[0, 1]

    while len(fib)<N:
        nextfib= fib[-1]+fib[-2]
        fib.append(nextfib)

    return fib

N = int(input())

fib=fibonacci(N)

print(" ".join(map(str, fib[:N])))
