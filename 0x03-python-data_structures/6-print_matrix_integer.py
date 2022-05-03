#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        last = 1
        for ii in i:
            if size == last:
                print(f"{ii}", end='')
            else:
                print(f"{ii} ", end='')
            last += 1
        print("")
