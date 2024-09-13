#!/usr/bin/python3
""" Divides all elements of a matrix by a given divisor and returns a new matrix with the results. """


def matrix_divided(matrix, div):
    """
    
    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor to divide all elements by.
    
    Returns:
        list of lists of float: A new matrix with all elements divided by `div`, rounded to 2 decimal places.
    
    Raises:
        TypeError: 
            - If matrix is not a list of lists of integers/floats.
            - If each row of the matrix does not have the same size.
            - If div is not a number (integer or float).
        ZeroDivisionError: 
            - If div is zero.
    
    Example:
        >>> matrix = [[1, 2], [3, 4]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Ensure all elements in the matrix are integers or floats
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Ensure all rows in the matrix have the same size
    row_size = len(matrix[0]) if matrix else 0
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Ensure divisor is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Ensure divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the division and round results to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
