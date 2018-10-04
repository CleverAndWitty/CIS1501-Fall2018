def sum_of_odd_numbers_from_1_to_n(n):
    sum = 0
    for number in range(1, n+1, 2):
        sum += number

    return sum