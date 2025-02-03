import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[0, 3, 6], [2, 4, 8], [], [1, 1, 2]]
        result = lab4.first_element(input)
        expected = [0, 2, 1]
        self.assertEqual(expected, result)
        # write a second test here

    def test_first_element_3(self):
        input = [[7, 14, 21], [8, 16, 24], [], [9, 18, 27]]
        result = lab4.first_element(input)
        expected = [7, 8, 9]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(1, 1), data.Point(2, 3), data.Point(5, 8)]
        result = lab4.x_coordinates(input)
        expected = [1, 2, 5]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(2.2, 1.0), data.Point(5.6, 6.7), data.Point(2.17, 3.14)]
        result = lab4.x_coordinates(input)
        expected = [2.2, 5.6, 2.17]
        self.assertEqual(expected, result)


    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(1, 1), data.Point(7, -3), data.Point(-100, 100), data.Point(-13, -85)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(1,1)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(0, 0), data.Point(-1, -1), data.Point(-10, 20), data.Point(-1, 1000)]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected, result)



    # Part 4
    def test_distance_1(self):
        result = lab4.distance(data.Point(0,0), data.Point(3, 4))
        expected = 5.0
        self.assertEqual(expected, result)


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
