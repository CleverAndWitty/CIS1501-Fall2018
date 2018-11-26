from unittest import TestCase
import Polygons


class TestPolygon(TestCase):
    def test_get_perimeter(self):
        test_polygon = Polygons.Polygon(3, [1, 2, 3])
        expected_perimeter = 6
        self.assertEqual(test_polygon.get_perimeter(), expected_perimeter)

    def test_get_area(self):
        test_polygon = Polygons.Polygon(3, [1, 2, 3])
        with self.assertRaises(NotImplementedError):
            test_polygon.get_area()
