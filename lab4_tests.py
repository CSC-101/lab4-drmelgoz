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


    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
