# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:24:19 2024

@author: khang
"""

import pytest
from mat_mul import multiply_matrices

# Test Example 1
matrix_A_1 = [[1, 2], [3, 4]]
matrix_B_1 = [[5, 6], [7, 8]]
expected_result_1 = [[19, 22], [43, 50]]
assert multiply_matrices(matrix_A_1, matrix_B_1) == expected_result_1, "Test Example 1 Failed"

# Test Example 2
matrix_A_2 = [[1, 2, 3], [4, 5, 6]]
matrix_B_2 = [[7, 8], [9, 10], [11, 12]]
expected_result_2 = [[58, 64], [139, 154]]
assert multiply_matrices(matrix_A_2, matrix_B_2) == expected_result_2, "Test Example 2 Failed"

# Test Example 3
matrix_A_3 = [[2, 4, 6], [8, 10, 12]]
matrix_B_3 = [[1, 3], [5, 7], [9, 11]]
expected_result_3 = [[76, 100], [166, 226]]
assert multiply_matrices(matrix_A_3, matrix_B_3) == expected_result_3, "Test Example 3 Failed"

# Test Example 4: Error - Mismatched matrix sizes
matrix_A_4 = [[1, 2], [3, 4]]
matrix_B_4 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
with pytest.raises(ValueError, match="Number of columns in A must be equal to number of rows in B for matrix multiplication."):
    multiply_matrices(matrix_A_4, matrix_B_4)

# Test Example 5: Null matrices
matrix_A_5 = [[0, 0], [0, 0]]
matrix_B_5 = [[0, 0], [0, 0]]
expected_result_5 = [[0, 0], [0, 0]]
assert multiply_matrices(matrix_A_5, matrix_B_5) == expected_result_5, "Test Example 5 Failed"

# Test Example 6: Matrices with negative numbers
matrix_A_6 = [[-1, -2, -3], [-4, -5, -6]]
matrix_B_6 = [[-7, -8], [-9, -10], [-11, -12]]
expected_result_6 = [[58, 64], [139, 154]]
assert multiply_matrices(matrix_A_6, matrix_B_6) == expected_result_6, "Test Example 6 Failed"

#Test Example 7: matrix * non-matrix
matrix_A_7 = [[1, 2], [3, 4]]
matrix_B_7 = 5  # Non-matrix input

with pytest.raises(ValueError, match="Invalid matrix dimensions for multiplication: B must be a matrix."):
    multiply_matrices(matrix_A_7, matrix_B_7)

print("All test examples passed!")