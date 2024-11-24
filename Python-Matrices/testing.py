def rref(matrix):
    """
    Calculates the Reduced Row Echelon Form of a matrix.
    """

    rows = len(matrix)
    cols = len(matrix[0])

    lead = 0
    for r in range(rows):
        if lead >= cols:
            return matrix

        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return matrix

        matrix[i], matrix[r] = matrix[r], matrix[i]

        lv = matrix[r][lead]
        matrix[r] = [x / lv for x in matrix[r]]

        for i in range(rows):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [x - lv * y for x, y in zip(matrix[i], matrix[r])]

        lead += 1

    return matrix

matrix = [[1, 2, -1, -4], 
          [2, 3, -1, -11], 
          [-2, 0, -3, 22]]
rref_matrix = rref(matrix)

print(rref_matrix)