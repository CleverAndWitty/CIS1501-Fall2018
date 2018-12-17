# source https://raw.githubusercontent.com/EricCharnesky/CIS1501-Fall2018/9a3d26277a3f166902618bc1a3af5fc1ed0a4a36/Week13/Week13.py
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
    return current


def sum_of_fibonacci_terms(nth):
    sum = 0
    for n in range(1,nth+1):
        sum += better_fib_iterative(n)
    return sum

print(sum_of_fibonacci_terms(5))
print(1+1+2+3+5)



class GradeCalculator:

    def __init__(self, curve):
        self.curve = curve

    def percentage_to_letter_grade(self, percentage):
        adjusted_percentage = percentage + self.curve

        if adjusted_percentage >= 94:
            return "A"
        if adjusted_percentage >= 90:
            return "A-"
        if adjusted_percentage >= 87:
            return "B+"
        if adjusted_percentage >= 83:
            return "B"
        if adjusted_percentage >= 80:
            return "B-"
        if adjusted_percentage >= 77:
            return "C+"
        if adjusted_percentage >= 73:
            return "C"
        if adjusted_percentage >= 70:
            return "C-"
        if adjusted_percentage >= 67:
            return "D+"
        if adjusted_percentage >= 63:
            return "D"
        if adjusted_percentage >= 60:
            return "D-"
        return "F"

gradeCalculator = GradeCalculator(5)

for percentage in range(53, 100, 5):
    print(percentage, ":", gradeCalculator.percentage_to_letter_grade(percentage))



def sum_of_values_on_chessboard_squares(color, two_dimensinal_list):
    sum = 0

    if color == 'white':
        offset = 1
    elif color == 'black':
        offset = 0
    else:
        return 0
    for row in two_dimensinal_list:
        for column_index in range(offset,8,2):
            sum += row[column_index]
        if offset == 1:
            offset = 0
        else:
            offset = 1

    return sum