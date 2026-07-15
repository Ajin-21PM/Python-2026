def factorial_normal(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

print(factorial_normal(5))

def factorial_recursivo(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))