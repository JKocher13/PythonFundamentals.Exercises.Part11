import shapes
import unittest

class TestShapes(unittest.TestCase):

    def test_area(self):
        rect = shapes.Rectangle(5, 6)
        expected = 30
        actual = rect.area()
        self.assertEqual(expected, actual)

     def test_perimeter(self):
     	rect = shapes.Rectangle(4,2)
     	expected = 12
     	actual = rect.perimeter()
     	self.assertEqual(expected, actual)
     	
class SquareTest(unittest.TestCase):
    def test_instantiation(self):
        self.assertTrue(issubclass(shapes.Square, shapes.Rectangle))
