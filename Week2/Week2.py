import math
import sys

print(sys.builtin_module_names)
names = ['Eric', 'Talia', 'Muhammad', 'Patrick', 'Numan', "Steven"]
print(names)
names[0] = 'Eric Charnesky'
print(names)
names.append("Bobby")
names.append("Mary")
names.insert(3, "John")
names.remove("John")

names.pop(0)
print(names)
print(min(names))

sales_totals_per_day = [ 1000, 1200, 900, 1000, 1500 ]

print("average sales:", end=' ')
print(sum(sales_totals_per_day) / len(sales_totals_per_day))

grades = {
    "Eric": 'A',
    "Talia": 'A',
    "Muhammed": 'A',
    "Patrick": 'F',
    "Patrick": 'A' # don't put duplicates in
}
print(grades)
grades['Numan'] = 'A'
grades['Patrick'] = 'A'
grades.pop('Patrick')

print(grades)


total_people = 75
dollars = 68
best_friend = 'Sydnie'


print("Your new friends are %s, %s, %s" % (names[1], names[2], names[4]))

print(math.pi)
