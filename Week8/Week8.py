names = ['Eric', 'Talia', 'Steven', 'Patrick', 'Mahad']
new_names = names[:]

new_names.remove('Eric')

for index in range(len(names)):
    if names[index] == "Eric":
        # don't remove items from a list while looping through it
        #names.pop(index)
        pass

chart = []
for row in range(1, 11):
    chart.append([])
    for col in range(1, 11):
        chart[row-1].append( row * col )

for row in chart:
    for item in row:
        #https://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-a-string
        print("{:2d}".format(item), end="")
        if item != row[-1]:
            print(" | ", end="")
    print()

numbers = [10,20,25,30]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

even_numbers_faster = \
    [number for number in numbers if (number % 2) == 0]

print(even_numbers)
print(even_numbers_faster)



grades = { 'Eric' : 'A', "Talia" : "A+" }

for key, value in grades.items():
    print(key, value)

for key in grades:
    print(key, grades[key])

