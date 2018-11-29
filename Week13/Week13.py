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


def _better_fib(targetNth, previous, current, currentNth):
    if targetNth == currentNth:
        return current
    return _better_fib(targetNth, current, previous+current, currentNth+1)

def better_fib(nth):
    if nth <= 0:
        return 0
    elif nth == 1 or nth == 2:
        return 1
    return _better_fib(nth, 1, 1, 2)

def better_fib_iterative(nth):
    if nth <= 0:
        return 0
    elif nth == 1 or nth == 2:
        return 1
    else:
        current = 1
        previous = 1
        currentNth = 2
        while currentNth != nth:
            next = current + previous
            previous = current
            current = next
            currentNth += 1



print(better_fib(40))