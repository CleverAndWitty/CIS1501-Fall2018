from unittest import TestCase
import Shapes


class TestTriangle(TestCase):
    def test_get_area_jackpot(self):
        triangle = Shapes.Triangle(10,10)
        another_triangle = Shapes.Triangle(10,10)
        self.assertEqual(triangle.get_area(), another_triangle.get_area())

    def test_get_area_fails(self):
        triangle = Shapes.Triangle(10, 10)
        self.assertEqual(5, triangle.get_area())