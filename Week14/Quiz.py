def sum_of_1_to_n(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_of_1_to_n(n-1)

for i in range(10):
    print(sum_of_1_to_n(i))