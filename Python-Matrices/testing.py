def rref(matrix):
    """
    Compute the Reduced Row Echelon Form (RREF) of a matrix.
    
    Parameters:
        matrix (list of list of floats): Input matrix.
        
    Returns:
        list of list of floats: Matrix in RREF.
    """
    # Number of rows and columns
    rows = len(matrix)  # Count the number of rows in the matrix
    cols = len(matrix[0])  # Count the number of columns in the matrix

    # Start with the first pivot position
    pivot_row = 0  # Index of the current pivot row
    for pivot_col in range(cols):  # Iterate through each column as a potential pivot column
        if pivot_row >= rows:  # If we've processed all rows, exit the loop
            break

        # Find the pivot row
        max_row = pivot_row  # Assume the current pivot row is the maximum
        for r in range(pivot_row + 1, rows):  # Check rows below the current pivot row
            if abs(matrix[r][pivot_col]) > abs(matrix[max_row][pivot_col]):  # Compare absolute values
                max_row = r  # Update the maximum row if a larger value is found

        # Swap rows to put the pivot row in place
        if matrix[max_row][pivot_col] != 0:  # Only swap if the pivot column is non-zero
            matrix[pivot_row], matrix[max_row] = matrix[max_row], matrix[pivot_row]  # Swap rows

            # Normalize the pivot row
            pivot = matrix[pivot_row][pivot_col]  # Get the pivot value
            matrix[pivot_row] = [x / pivot for x in matrix[pivot_row]]  # Divide entire row by pivot

            # Eliminate below and above
            for r in range(rows):  # Iterate through all rows to eliminate the pivot column
                if r != pivot_row:  # Skip the pivot row itself
                    factor = matrix[r][pivot_col]  # Factor to eliminate the current column
                    matrix[r] = [matrix[r][c] - factor * matrix[pivot_row][c] for c in range(cols)]  # Update row

            # Move to the next pivot row
            pivot_row += 1  # Increment the pivot row index

    return matrix  # Return the matrix in RREF

def invert_matrix(matrix):
    """
    Compute the inverse of a square matrix using RREF.

    Parameters:
        matrix (list of list of floats): Input square matrix.

    Returns:
        list of list of floats: Inverse of the matrix, or None if the matrix is not invertible.
    """
    # Check if the matrix is square
    n = len(matrix)  # Get the number of rows in the matrix
    if any(len(row) != n for row in matrix):  # Ensure all rows have the same length as the number of rows
        raise ValueError("Matrix must be square.")  # Raise an error if the matrix is not square

    # Create an augmented matrix [A | I]
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]  # Append identity matrix

    # Compute RREF of the augmented matrix
    rref_matrix = rref(augmented_matrix)  # Call the RREF function

    # Check if the left side is the identity matrix
    for i in range(n):  # Iterate through each row
        if not all(abs(rref_matrix[i][j] - (1 if i == j else 0)) < 1e-9 for j in range(n)):  # Check identity condition
            return None  # Matrix is not invertible

    # Check for rows of zeros in the RREF matrix
    for row in rref_matrix:  # Iterate through rows
        if all(num == 0 for num in rref_matrix.rows):  # Check if all entries in the original matrix portion are zero
            raise ValueError("Matrix has a row of zeros and is singular.")  # Raises an error for singular matrix

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in rref_matrix]  # Extract the right side as the inverse

    return inverse_matrix  # Return the inverse matrix

# Example usage
if __name__ == "__main__":
    # Define individual matrices
    matrix_2x2 = [[4, 7], [2, 6]]  # 2x2 matrix
    matrix_3x3 = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]  # 3x3 matrix
    matrix_4x4 = [[7, 2, 1, 0], [0, 3, -1, 2], [1, 0, 1, 1], [2, 1, 3, 2]]  # 4x4 matrix
    matrix_3x4 = [[2, 4, 1, 3], [0, 1, 5, 2], [1, 0, 3, 1]]  # 3x4 matrix

    # Process 2x2 matrix
    print("\nOriginal 2x2 matrix:")
    for row in matrix_2x2:
        print(row)

    rref_result_2x2 = rref([row[:] for row in matrix_2x2])
    print("\nRREF of 2x2 matrix:")
    for row in rref_result_2x2:
        print(row)

    # Process 3x3 matrix
    print("\nOriginal 3x3 matrix:")
    for row in matrix_3x3:
        print(row)

    rref_result_3x3 = rref([row[:] for row in matrix_3x3])
    print("\nRREF of 3x3 matrix:")
    for row in rref_result_3x3:
        print(row)

    # Process 4x4 matrix
    print("\nOriginal 4x4 matrix:")
    for row in matrix_4x4:
        print(row)

    rref_result_4x4 = rref([row[:] for row in matrix_4x4])
    print("\nRREF of 4x4 matrix:")
    for row in rref_result_4x4:
        print(row)

    # Process 3x4 matrix
    print("\nOriginal 3x4 matrix:")
    for row in matrix_3x4:
        print(row)

    rref_result_3x4 = rref([row[:] for row in matrix_3x4])
    print("\nRREF of 3x4 matrix:")
    for row in rref_result_3x4:
        print(row)

    # Test invert function with a 2x2 matrix
    try:
        inverse = invert_matrix(matrix_2x2)  # Attempt to invert the 2x2 matrix

        if inverse:  # If inversion was successful
            print("\nInverse of 2x2 matrix:")
            for row in inverse:  # Print each row of the inverse
                print(row)
    except ValueError as e:  # Handle singular matrix error
        print(f"\nError: {e}")
