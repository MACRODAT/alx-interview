#!/usr/bin/python3
'''Pascal triangle'''


def pascal_triangle(n):
    '''
    Function that generates pascal triangles
    '''
    pascal_triangle = list()

    if n <= 0:
        return pascal_triangle

    if n > 0:
        pascal_triangle.append([1])

    if n > 1:
        pascal_triangle.append([1, 1])

    for x in range(3, n+1):
        pascal_triangle.append([0] * x)

        pascal_triangle[x-1][0] = 1
        pascal_triangle[x-1][x-1] = 1

        for y in range(1, x-1):
            pascal_triangle[x-1][y] = \
                pascal_triangle[x-2][y-1] + pascal_triangle[x-2][y]

    return pascal_triangle
