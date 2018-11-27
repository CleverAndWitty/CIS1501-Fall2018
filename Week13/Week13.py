def factorial(n):
    if n < 1:
        return 0
    total = n
    while n > 1:
        n -= 1
        total *= n
    return total

def factorial_recursive(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial(5))
print(factorial_recursive(5))


def fib(nth):
    if nth <= 0:
        return 0
    elif nth == 1 or nth == 2:
        return 1
    else:
        return fib(nth-1) + fib(nth-2)

print(fib(40))