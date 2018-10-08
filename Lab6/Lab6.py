def add_students():
    students = {}
    name = ""
    while name.lower() != "done":
        name = input("Enter a student name, or DONE to stop: ")
        if name.lower() != "done":
            students[name] = 0

    return students


def add_scores(students):
    for student in students:
        students[student] = int(input("Please enter the score for " + student + ": "))


def menu():
    choice = ""
    while choice not in ("1", "2", "3", "4", "5"):
        print("1 - Get student's score")
        print("2 - Get high score")
        print("3 - Get average score")
        print("4 - Get lowest score")
        print("5 - Quit")
        choice = input()
    return choice


def get_score_for_student(students):
    name = input("Enter a name to lookup")
    if name in students:
        return name + "'s score: " + str(students[name])
    else:
        return "NOT FOUND"


def get_max(students):
    highest = 0
    for student in students:
        if highest < students[student]:
            highest = students[student]

    return highest


def get_min(students):
    lowest = 100
    for student in students:
        if lowest > students[student]:
            lowest = students[student]

    return lowest


def get_average(students):
    total = 0
    for student in students:
        total += students[student]

    return total / len(students)


students = add_students()
add_scores(students)
choice = ""
while choice != "5":
    choice = menu()
    if choice == "1":
        print(get_score_for_student(students), "\n")
    elif choice == "2":
        print("Highest score:", get_max(students), "\n")
    elif choice == "3":
        print("Average score:", get_average(students), "\n")
    elif choice == "4":
        print("Lowest score:", get_min(students), "\n")


