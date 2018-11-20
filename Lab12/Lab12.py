
class Assignment:

    def __init__(self, name, possible_points, earned_points=0):
        self.name = name
        self.possible_points = possible_points
        self.earned_points = earned_points

    def __str__(self):
        return "Name: {} - Possible Points: {} - Earned Points: {}".format(self.name, self.possible_points, self.earned_points)


class Student:

    def __init__(self, name):
        self.name = name
        self.assignments = []

    def get_score(self):
        total_points = 0
        earned_points = 0
        for assignment in self.assignments:
            total_points += assignment.possible_points
            earned_points += assignment.earned_points
        return earned_points / total_points * 100

    def __str__(self):
        return "Name: {} - Assignemnts:\n{}".format(self.name, "\n".join([str(a) for a in self.assignments ]))


class Gradebook:

    def __init__(self):
        self.students = []

    def save(self):
        file_name = input("Enter the name to save the gradebook as: ")
        with open(file_name, 'w') as saved_file:
            saved_file.write(str(self))

    def add_student(self):
        name = input("Enter the student's name: ")
        self.students.append(Student(name))

    def get_highest_score(self):
        highest = self.students[0]
        for student in self.students:
            if student.get_score() > highest.get_score():
                highest = student
        print("{} has the highest score: {}"
              .format(highest.name, highest.get_score()))

    def add_assignment(self):
        name = input("Enter the assignment name: ")
        possible_points = int(input("Enter the total points possible: "))
        for student in self.students:
            for assignment in student.assignments:
                if assignment.name == name:
                    break
            else:
                student.assignments.append(Assignment(name, possible_points))

    def score_stduent(self):
        name = input("Enter the student's name to score: ")

        for student in self.students:
            if name == student.name:
                for assigment in student.assignments:
                    score = input("Enter score for {} "
                                    "- Max points {}: "
                                    .format(assigment.name,
                                    assigment.possible_points))
                    assigment.earned_points = int(score)

    def __str__(self):
        return "\n".join([str(s) for s in self.students])

    def load(self):
        file_name = input("Enter the name of the file to load: ")
        with open(file_name) as input_file:
            lines = input_file.readlines()


        current_student_index = 0
        while current_student_index < len(lines):
            line = lines[current_student_index]
            student = Student(line[6:line.index(" - Assignemnts:")])
            self.students.append(student)
            line = lines[current_student_index+1]
            assignment_count = 1
            while not line.endswith(" - Assignemnts:\n"):
                name = line[6:line.index(" - Possible Points:")]
                possible_points = int(line[line.index(" - Possible Points: ") + 20: line.index(" - Earned Points: ")])
                earned_points = int(line[line.index(" - Earned Points: ") + 18:])
                student.assignments.append(Assignment(name, possible_points, earned_points))
                assignment_count += 1
                if current_student_index + assignment_count >= len(lines):
                    break
                line = lines[current_student_index + assignment_count]
            current_student_index += assignment_count





gradebook = Gradebook()
gradebook.load()
gradebook.add_student()
gradebook.add_student()
gradebook.add_assignment()
gradebook.add_assignment()
gradebook.score_stduent()
gradebook.score_stduent()
gradebook.save()

print(gradebook)