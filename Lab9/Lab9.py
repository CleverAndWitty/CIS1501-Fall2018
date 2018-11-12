class Assignment:

    def __init__(self, name, possible_points, earned_points=0):
        self.name = name
        self.possible_points = possible_points
        self.earned_points = earned_points


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


class Gradebook:

    def __init__(self):
        self.students = []

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


gradebook = Gradebook()
gradebook.add_student()
gradebook.add_assignment()
gradebook.score_stduent()
gradebook.get_highest_score()