from unittest import TestCase
import Review

class TestGradeCalculator(TestCase):

    def test_percentage_to_letter_grade_0_curve(self):
        gradeCalculator = Review.GradeCalculator(0)
        self.assertEquals("F", gradeCalculator.percentage_to_letter_grade(50))
        self.assertEquals("D-", gradeCalculator.percentage_to_letter_grade(62))
        self.assertEquals("D", gradeCalculator.percentage_to_letter_grade(65))
        self.assertEquals("D+", gradeCalculator.percentage_to_letter_grade(68))
        self.assertEquals("C-", gradeCalculator.percentage_to_letter_grade(72))
        self.assertEquals("C", gradeCalculator.percentage_to_letter_grade(75))
        self.assertEquals("C+", gradeCalculator.percentage_to_letter_grade(78))
        self.assertEquals("B-", gradeCalculator.percentage_to_letter_grade(82))
        self.assertEquals("B", gradeCalculator.percentage_to_letter_grade(85))
        self.assertEquals("B+", gradeCalculator.percentage_to_letter_grade(88))
        self.assertEquals("A-", gradeCalculator.percentage_to_letter_grade(92))
        self.assertEquals("A", gradeCalculator.percentage_to_letter_grade(95))

    def test_percentage_to_letter_grade_10_curve(self):
        gradeCalculator = Review.GradeCalculator(10)
        self.assertEquals("F", gradeCalculator.percentage_to_letter_grade(40))
        self.assertEquals("D-", gradeCalculator.percentage_to_letter_grade(52))
        self.assertEquals("D", gradeCalculator.percentage_to_letter_grade(55))
        self.assertEquals("D+", gradeCalculator.percentage_to_letter_grade(58))
        self.assertEquals("C-", gradeCalculator.percentage_to_letter_grade(62))
        self.assertEquals("C", gradeCalculator.percentage_to_letter_grade(65))
        self.assertEquals("C+", gradeCalculator.percentage_to_letter_grade(68))
        self.assertEquals("B-", gradeCalculator.percentage_to_letter_grade(72))
        self.assertEquals("B", gradeCalculator.percentage_to_letter_grade(75))
        self.assertEquals("B+", gradeCalculator.percentage_to_letter_grade(78))
        self.assertEquals("A-", gradeCalculator.percentage_to_letter_grade(82))
        self.assertEquals("A", gradeCalculator.percentage_to_letter_grade(85))



