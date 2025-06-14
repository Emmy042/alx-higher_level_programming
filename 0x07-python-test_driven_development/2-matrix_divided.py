#!/usr/bin/python3

def matrix_divided(matrix, div):
    
    if not isinstance(matrix, list) or any(
    not isinstance(row, list) or
    any(not isinstance(num, (int, float)) for num in row)
    for row in matrix
):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
