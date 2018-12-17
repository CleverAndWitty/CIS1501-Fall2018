from unittest import TestCase
import Review

class TestSum_of_values_on_chessboard_squares(TestCase):
    def test_sum_of_values_on_chessboard_squares(self):
        board = [
            [1,2,3,4,5,6,7,8],
            [2,4,6,8,10,12,14,16],
            [15,13,11,9,7,5,3,1],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [8,7,6,5,4,3,2,1],
            [10,20,30,40,50,60,70,80],
            [1,2,1,2,1,2,1,2]
        ]
        for row in board:
            print(sum(row))
        self.assertEqual(308,Review.sum_of_values_on_chessboard_squares('white', board))
        self.assertEqual(280, Review.sum_of_values_on_chessboard_squares('black', board))
