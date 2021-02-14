matrix =
[[3,2,-1],
 [6,4,9],
 [2,6,-1]]


def zeroMinusOnes(matrix):
    lines = [False] * len(matrix)
    columns = [False] * len(matrix[0])

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == -1:
                lines[i] = True
                columns[j] = True

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if lines[i] or columns[j]:
                matrix[i][j] = 0

if __name__ == '__main__':
    zeroMinusOnes(matrix)
    print matrix
