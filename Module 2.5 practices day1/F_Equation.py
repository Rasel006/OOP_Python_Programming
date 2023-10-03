def calculate_equation_result(X, N):
    result = -1
    term = 1
    for i in range(0, N+1,2):
        result += term
        term *= X
        term *= X
    return result

X, N = map(int, input().split())

result = calculate_equation_result(X, N)
print(result)
