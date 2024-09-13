#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and rounds to 2 decimal places.
    
    Args:
        matrix (list of lists): A matrix where each element is an integer or float.
        div (int or float): The divisor by which the matrix elements will be divided.
    
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, or if
                   each row of the matrix does not have the same size, or if div is
                   not a number (integer or float).
        ZeroDivisionError: If div is zero.
    
    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimal places.
    
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(item / div, 2) for item in row] for row in matrix]
