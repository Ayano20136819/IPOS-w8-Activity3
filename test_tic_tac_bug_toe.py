# -------------------------------
#
# Folder: 
# Filename: 
# Author: Ayano SASAKIDO
# Version 0.0
# Created: 
#
# -------------------------------

import unittest
import tic_tac_bug_toe

class TestTicTac(unittest.TestCase):
    def test_check_win_X(self):
        board = [['X', 'X', 'X'],
                 ['O', 'O', ' '],
                 [' ', ' ', ' ']]
        self.assertTrue(tic_tac_bug_toe.is_win(board, "X"))

    def test_check_win_O(self):
        board = [['X', ' ', 'X'],
                 ['O', 'O', 'O'],
                 [' ', ' ', ' ']]
        self.assertTrue(tic_tac_bug_toe.is_win(board, "O"))
