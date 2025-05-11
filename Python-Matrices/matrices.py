# Program Name: MatrixMasterChrisSuy
# Student Name: Chris Suy
# Course: CS-X
# Instructor: Mr. Campbell, Ms. Iverson, Mr. Carr
# Date: 11/18/24
# I pledge my honor
# Code version: 0.6

#TO-DO: 
"""
1) Program and refine RREF code
2) Program and refine Matrix Inversion
3) Add user input for Ms. Iverson
4) Bulletproof code (make it so Ms. Iverson cannot forcibly break the code/attempt an unattemptable math operation)
5) Code Xtra challenges
"""
#Note: shift + enter opens up an instance of the code being tested ;)

import time

class MatrixMaster:

# Defines the matrix and its attributes (rows, columns, and matrix information)
    def __init__(self, rows, cols):
        """
        This method initializes any matrix as a class object.

        Variables:
        self.rows: the # of "rows" in an initialized matrix
        self.cols: the # of "columns" in an initialized matrix
        self.data: the values of the inputted matrix stored as class values
        """
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

# The following methods direct the matrix manipulation of one or two matrices. 
# Matrix printing. Prints out the current instance of the matrix being returned/accessed.
    def print_matrix(self):
        """
        This method prints the current matrix being manipulated. 
        It takes in self (the matrix being inputted), and then formats and prints out the formatted matrix.

        Variables:
        i: temporary variable that iterates through the # of rows in the inputted matrix
        j: temporary variable that iterates through the # of columns in the inputted matrix
        self.data[i][j]: the current matrix coordinate (AKA the current indice/index) being accessed of self

        Returns: 
        - A formatted matrix of the current matrix being accessed
        """

        for i in range(self.rows): # Iterates through all rows in the matrix
            for j in range(self.cols): # Iterates through all cols in the row
                print(self.data[i][j], end=" ") # Prints and formats each value of the matrix in order with spaces between each value
            print() # Prints the formatted matrix to the terminal/console

# Matrix addition. Adds two different matrices together
    def plus(self, alice):
        """
        This method prints out the sum of two square matrices that come from the addition of 2 square matrices.
        It takes in two arguments, self and alice. Self is the 1st matrix, and alice is the 2nd matrix.
        If they are square matrices (meaning they have the same amount of rows and columns), their values
        will be added together. If these conditions are met, the resulting matrix is then returned.  
        Otherwise, an exception is raised explaining that the inputted matrices are not square, and therefore 
        cannot be added. The resulting matrix is then returned. 

        Variables:
        alice.rows: the # of rows in the 2nd matrix
        alice.cols: the # of columns in the 2nd matrix
        self.rows: the # of rows in the 1st matrix
        self.cols: the # of columns in the 1st matrix
        i: temporary variable that iterates through the # of rows in the 2nd matrix
        j: temporary variable that iterates through the # of columns in the 2nd matrix
        alice.data[i][j]: the current matrix coordinate (AKA the current indice/index) being accessed of the 2nd matrix
        self.data[i][j]: the current matrix coordinate (AKA the current indice/index) being accessed of the 1st matrix
        newMatrix.data[i][j]: the current matrix coordinate (AKA the current indice/index) that contains the summed up values of alice.data[i][j] and self.data[i][j] being accessed of the new matrix

        Returns: 
        - A matrix with the summed values of two matrices added to one another
        """

        
        if alice.rows != self.rows or alice.cols != self.cols: # Checks if the 2nd matrix's columns or rows are not equal the 1st matrix's columns or rows
            raise Exception("Matrices are not the same size! Function halted") # Raises an exception explaining that the matrices are not square
        newMatrix = MatrixMaster(self.rows, self.cols) # Creates a new matrix with the same dimensions as both matrices by utilizing 
        for i in range(alice.rows): # Iterates through all rows in the 2nd matrix
            for j in range(alice.cols): # Iterates through all columns in the row
                newMatrix.data[i][j] = alice.data[i][j] + self.data[i][j] # The new matrix's current index value will be the summed values of the 1st and 2nd matrix's combined
        return newMatrix # Returns the newly created matrix
    
# Matrix multiplication. Multiplies two different matrices together
    def times(self, alice):
        """
        This method prints out the product of two matrices. 
        To do so, the matrices must meet a simple rule, that being that the 
        columns of the 1st matrix must be equal to the rows of the 2nd matrix. If this isn't true, then the matrices cannot be 
        multiplied. If these conditions are met, the resulting matrix is then returned, with the # of rows of the 1st matrix
        and the # of columns of the 2nd matrix. The resulting matrix is then returned.

        Variables:


        Returns:
        - A matrix with the rows of the 1st matrix and the columns of the 2nd matrix, and the multiplied values
          of the two matrices 
        """
        if self.cols != alice.rows:
            raise Exception("Error! Columns in one matrix not equal to the rows of other matrix. Function halted.")
        else:
            newMatrix = MatrixMaster(self.rows, alice.cols) # Creates a new matrix with the rows of the 1st matrix and the columns of the 2nd matrix
            for i in range(alice.cols): # For every row entry in the 2nd matrix
                for j in range(self.rows): # For every row entry in the 1st matrix
                    for k in range(self.cols): # For every column entry in the 1st matrix
                        newMatrix.data[i][j] += self.data[i][k] * alice.data[k][j] # Manipulates the new matrix's data values 
            return newMatrix # Returns the newly created matrix
        
# Row switching. Switches two rows of a matrix.
    def switchRows(self, row_one_num, row_two_num):
        # List indices begin at 0. 1 is subtracted from each entered row number to account for this.
        row1_num = row_one_num - 1
        row2_num = row_two_num - 1

        #If the row numbers are out of bounds (less than 0 or exeeds the row/col indice count)
        if (row1_num < 0 or row1_num > self.rows) or (row2_num < 0 or row2_num > self.rows):

            #Throws an error
            raise Exception("Error! One or more of the selected row numbers exceeds the list range of the inputted matrix. Function halted.")
        else:

            # Creates a copy of the exising matrix to be manipulated
            newMatrix = MatrixMaster(self.rows, self.cols)

            # For every row entry:
            for i in range(self.rows):
                
                # For every column entry:
                for j in range(self.cols):

                    #Sets the new matrix's data to be exactly like the old matrix's data
                    newMatrix.data[i][j] = self.data[i][j]

                    #Swaps each row by copying that row's data directly onto that row's element values
                    newMatrix.data[row2_num][j] = self.data[row1_num][j]
                    newMatrix.data[row1_num][j] = self.data[row2_num][j]
            return newMatrix
                
# Scalar row multiplication. Takes the scalar multiplier and the number of the row and multiplies all elements of that row.
    def scalarTimesRow(self, scalar, row_num):
        scalar = float(scalar)
        row_number = float(row_num - 1)

        if isinstance(scalar, int) and isinstance(row_number, int):
            """
            
            """
            newMatrix = MatrixMaster(self.rows, self.cols)
            # For every row entry
            for i in range(self.rows):
                for j in range(self.cols):
                    newMatrix.data[i][j] = self.data[i][j] # Set the new matrix's data to be exactly like the old matrix's data
                    newMatrix.data[int(row_number)][j] = self.data[int(row_number)][j] * scalar
            return newMatrix
        else:
            raise Exception("Error! One or more inputted values are not valid numerical inputs. Function halted.")
        
    def linearCombRows(self, scalar, row_one_num, row_two_num):
        """
        Adds a scalar multiple
        
        Variables:

        Returns:

        
        """
        scalar = float(scalar)
        row1 = float(row_one_num - 1)
        row2 = float(row_two_num - 1)

        if isinstance(scalar, float) and isinstance(row1, float) and isinstance(row2, float): 
            newMatrix = MatrixMaster(self.rows, self.cols)
            
            # Itereates
            for i in range(self.rows): # For every row in the matrix
                for j in range(self.cols): # For every column in each row
                    newMatrix.data[i][j] = self.data[i][j] # Set the new matrix's data to be exactly like the old matrix's data
                    newMatrix.data[int(row2)][j] = (self.data[int(row1)][j] * scalar) + self.data[int(row2)][j]
            return newMatrix # Returns the 
        else:
            raise Exception("Error! One or more inputted values are not valid numerical inputs. Function halted.")

# RREF (Reduced Row Echelon Form). Finds solutions to systems of equations. 
    def rowReduce(self):
        """
        Calculates the RREF of a matrix. 
        The algorithm performs the following steps:
        1) Finds the pivot colum and the 1st pivot value

        Variables:

        Returns:
        """

        # Number of rows in self (the matrix)
        rows = self.rows

        # Number of columns in self (the matrix)
        cols = self.cols

        # Starts with the 1st pivot position
        pivot_row = 0 # Index of the current pivot row
        for pivot_col in range(cols): # Iterate through each column as a potential pivot column
            if pivot_row >= rows: # If all the rows have been processed, then finish and return the processed matrix
                return self

            # Find the pivot row
            max_row = pivot_row # Assume the current pivot row is the maximum
            for r in range(pivot_row + 1, rows): # Checks the rows below the current pivot row
                if abs(self.data[r][pivot_col]) > abs(self.data[max_row][pivot_col]): # Compare absolute values of each pivot column
                    max_row = r # Update the maximum row if a larger value is found
            
            # Swap out the rows to put the pivot row in place
            if self.data[max_row][pivot_col] != 0: # Only swap if the pivot column is more than 0
                self.data[pivot_row], self.data[max_row] = self.data[max_row], self.data[pivot_row] # Swap the rows of the pivot and max rows with each other

                # Normalizes teh pivot row by using some simple row division
                pivot = self.data[pivot_row][pivot_col] 
                self.data[pivot_row] = [x / pivot for x in self.data[pivot_row]]

            # ELminate the numbers above and below the pivot numbers
            for r in range(rows): # Iterate through all the rows to eliminate the pivot columns left
                if r != pivot_row: # Skip the pivot row itself
                    factor = self.data[r][pivot_col] # Finds the factor to eliminate the current column
                    self.data[r] = [self.data[r][c] - factor * self.data[pivot_row][c] for c in range(cols)] # Updates the row data

            # Move to the next pivot row by incrementing it by 1
            pivot_row += 1 # Adds one to the pivot row index

        return self # Returns the changed matrix
                
# Matrix Inversion. Finds the inverse of a current matrix via switching the identity matrix with the called matrix via row operations, thereby deriving the inverse once switched.
    def invert(self):
        """
        Variables:

        Returns:


        """
        # Check if the matrix is square
        row_count = self.rows  # Get the number of rows in the matrix
        if self.rows != self.cols:  # Ensure all rows have the same length as the number of rows
            raise ValueError("Matrix must be square to be invertible. Function halted.")  # Raise an error if the matrix is not square

        # Create an augmented matrix [A | I]
        identity_matrix = MatrixMaster(self.rows, self.cols)
        for row in range(self.rows):
            identity_matrix.data[row][row] = 1
        
        augmented_matrix = MatrixMaster(self.rows, 2 * self.cols)
        for row in range(self.rows):
            augmented_matrix.data[row] = self.data[row] + identity_matrix.data[row]

        augmented_matrix.rowReduce()
        for row in augmented_matrix.data:
            if all(num == 0 for num in row):
                raise Exception("Matrix is singular and cannot be inverted")
            else:
                return augmented_matrix
            
# Example usage
if __name__ == "__main__":
    trixie = MatrixMaster(2, 3)
    trixie.data = [[1, 2, 3], 
                   [4, 5, 6]]
    alice = MatrixMaster(3, 2)
    alice.data = [[7, 8], 
                  [9, 10], 
                  [11, 12]]
    tire = MatrixMaster(5, 6)
    tire.data = [[0, 10, 0, 0, 40, 20],
                 [0, 0, 15, 0, 0, 20],
                 [0, 10, 0, 0, 0, 50],
                 [0, -1, 0, 1, 1, 0],
                 [-1, 0, 1, 1, 1, 0]]
    safer = MatrixMaster(3, 3)
    safer.data = [[0, 1, 2], 
               [0, 2, 3],
               [0, 4, 5]]
    ae = MatrixMaster(2, 2)
    ae.data = [[4, 7], 
               [2, 6]]
    a = MatrixMaster(3, 3)
    a.data = [[2, 3, 2], [1, 0, 3], [2, 2, 3]]
    b = MatrixMaster(4, 4)
    b.data = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 4, 0], [0, 0, 0, 5]]

    s = MatrixMaster(3, 3)
    s.data = [[2, 3, 2], [1, 0, 3], [2, 2, 3]]

    f = MatrixMaster(3, 3)
    f.data = [[-6, -5, 9], [3, 2, -4], [2, 2, -3]]

    mia = MatrixMaster(2, 3)
    mia.data = [[1, 2, 3], [0, 0, 1]]

    kai = MatrixMaster(3, 1)
    kai.data = [[1], [1], [-1]]

    e = MatrixMaster(3, 4)
    e.data = [[2, 3, 2, -1], [1, 0, 3, 1], [2, 0, 6, 2]]
    
    #trixie.print_matrix() #-> Prints the current instance of trixie
    #trixie.plus(alice).print_matrix() #-> Throws an error (matrices must have same cols and rows to add)
    #alice.plus(trixie).print_matrix() #-> Throws an error (matrices must have same cols and rows to add)
    #mia.times(kai).print_matrix() #-> Creates a matrix with a 1st matrix's rows, and a 2nd matrix's cols
    #trixie.scalarTimesRow(2.0, 2).print_matrix() #-> Multiplies all values in the current matrix by 2
    #alice.linearCombRows(.5, 3, 2).print_matrix()
    #trixie.switchRows(1, 2).print_matrix() #-> Switches rows 1 and 2 with each other in the current matrix
    e.rowReduce().print_matrix() #-> Takes the Row Reduced Echelon Form (RREF) of the current matrix
    #b.invert().print_matrix()





    #try:
    #rows = int(input("How many rows would you like? Enter your response here: "))
    #cols = int(input("How many columns would you like? Enter your response here: "))

    #if isinstance(rows, int) and isinstance(cols, int):
        #print("Thank you. Please enter in your matrice's values now")
        #matrix = MatrixMaster(rows, cols)
        #for x in range(rows):
            #for y in range(cols):
                #indice_val = int(input(f"Enter the value for row {x+1}, column {y+1}: "))
                #matrix.data[x][y] = int(indice_val)

            #print("The Original Matrix:")        
            #matrix.print_matrix()
            
            #try:
                #inverse = tire.invert()  # Attempt to invert the 2x2 matrix

                #if inverse:  # If inversion was successful
                    #print("\nInverse of 2x2 matrix:")
                #for row in inverse:  # Print each row of the inverse
                    #print(row)
            #except ValueError as e:  # Handle singular matrix error
                #print(f"\nError: {e}")
            #print("""You have the matrix manipulation methods at your disposal:
                      #1) 
                      #2)
                      #3) Matrix Addition
                      #4) Matrix Multiplication
                      #5) Scalar Row Multiplication
                      #6) Row Switching
                      #7) RREF (Reduced Row Echelon Form)
                      #8) Matrix Inversion""")
            #try:
                #selection = int(input("Enter your number input here:"))
                #if isinstance(selection, int):
                    #if selection == 1:
                        #matrix.print_matrix()
                    #elif selection == 2:
                        #pass
                    #elif selection == 3:

                #else:
                    #raise ValueError
            #except ValueError:
                #print("Error. Please enter in numbers")
        #else:
            #raise ValueError
    #except ValueError:
        #print("Error. Please enter in numbers.")



    

