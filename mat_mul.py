"""
This function takes in 2 matrices, and will compute the final dot product of those 2 matrices. Function
will raise error if matrix dimensions don't match, as well as a scalar with a matrix. 

Approach: first check if both matrix inputs are actual matrices and not a scalar. It then goes through all elements
in each matrix and checking if all elements in the matrix is correct container type. Next it checks the dimensions, 
and if the dimensions doesn't work then it raises error. If we go through all of this without error, we can finally
compute the dot product of the 2 matrices by initializing a 3rd matrix (this will be our result matrix) to be 0's with 
the correct dimension, then go  through each element of the matrix inputs A & B, multiply them and insert them into 
our final result matrix. 
"""

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def multiply_matrices(A, B):
    if isinstance(A, (int, float)) or not all(isinstance(row, (list, tuple)) for row in A):
        logging.error("Invalid matrix dimensions for multiplication: A must be a matrix.")
        raise ValueError("Invalid matrix dimensions for multiplication: A must be a matrix.")
        
    if isinstance(B, (int, float)) or not all(isinstance(row, (list, tuple)) for row in B):
        logging.error("Invalid matrix dimensions for multiplication: B must be a matrix.")
        raise ValueError("Invalid matrix dimensions for multiplication: B must be a matrix.")
        
    # Get the number of rows and columns for each matrix
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        logging.error("Number of columns in A must be equal to number of rows in B for matrix multiplication.")
        raise ValueError("Number of columns in A must be equal to number of rows in B for matrix multiplication.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result