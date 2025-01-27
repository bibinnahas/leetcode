def rotate(matrix: list[list[int]]):
    # transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for row in matrix:
        row.reverse()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
