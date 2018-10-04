def odd_minus_even(list):
    sum = 0
    for index, value in enumerate(list):
        if index % 2 == 1:
            sum += value
        else:
            sum -= value

    return sum