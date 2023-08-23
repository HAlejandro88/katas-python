import unittest
from pangrams import pangrams
from diagona_diference import diagonal_difference

class TestPangrams(unittest.TestCase):
    
    def test_pangrams_is_true(self):
        self.assertEqual(pangrams('We promptly judged antique ivory buckles for the next prize'), 'pangram')

    def test_pangrams_is_false(self):
        self.assertEqual(pangrams('We promptly judged antique ivory buckles for the prize'), 'not pangram')



class TestDiagonalDifference(unittest.TestCase):

    def test_should_be_return_one(self):
        self.assertEqual(diagonal_difference([[4], [-1 ,1 ,-7, -8], [-10, -8 ,-5, -2], [0, 9 ,7 ,-1], [4, 4, -2, 1] ]), 1)


if __name__ == '__main__':
    unittest.main()



