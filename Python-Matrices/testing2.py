def augmented_identity_matrix(n):
    """Creates an n x 2n augmented identity matrix."""

    matrix = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        matrix.append(row + row)  # Append the row and its identity part
    return matrix

# Example
n = 3
result = augmented_identity_matrix(n)
for row in result:
    print(row)