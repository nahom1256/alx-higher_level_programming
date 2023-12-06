#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for l in matrix:
        squared.append([c**2 for c in l])
    return squared
