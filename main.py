__author__ = 'randxie'
import numpy as np
from Solver import PuzzleSolver

# Test case 1 (takes 0.0121s)
start = np.array([[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]])

# the following test case takes much longer time due to the inefficient implementation

# Test Case 2
# start = np.array([[2,5,13,12],[1,0,3,15],[9,7,14,6],[10,11,8,4]])

# Test Case 3
# start = np.array([[5,2,4,8],[10,0,3,14],[13,6,11,12],[1,15,9,7]])

# Test Case 4
# start = np.array([[11,4,12,2],[5,10,3,15],[14,1,6,7],[0,9,8,13]])

# Test Case 5
# start = np.array([[5,8,7,11],[1,6,12,2],[9,0,13,10],[14,3,4,15]])

dest = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

my_solver = PuzzleSolver(start,dest)
my_solver.SolvePuzzle()
my_solver.AnimateMove()
