# Program Name: MatrixMasterChrisSuy
# Student Name: Chris Suy
# Course: CS-X
# Instructor: Mr. Campbell, Ms. Iverson, Mr. Carr
# Date: 11/18/24
# I pledge my honor
# Code version: 

class MatrixMaster:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

# The following methods direct the matrix manipulation of one or two matrices. 


# Matrix printing. Prints out the current instance of the matrix being returned/accessed.
    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print()

# Matrix addition. Adds two different matrices together
    def plus(self, alice):
        if alice.rows != self.rows or alice.cols != self.cols: 
            raise Exception("Matrices are not the same size! Function halted")
        newMatrix = MatrixMaster(self.rows, self.cols)
        for i in range(alice.rows):
            for j in range(alice.cols):
                newMatrix.data[i][j] = alice.data[i][j] + self.data[i][j]
        return newMatrix
    
# Matrix multiplication. Multiplies two different matrices together
    def times(self, alice):
        if self.cols != alice.rows:
            raise Exception("Error! Columns in one matrix not equal to the rows of other matrix. Function halted.")
        else:
            newMatrix = MatrixMaster(self.rows, alice.cols)
            for i in range(alice.cols):
                for j in range(self.rows):
                    for k in range(self.cols):
                        newMatrix.data[i][j] += self.data[i][k] * alice.data[k][j]
            return newMatrix
        
# Scalar row multiplication. Takes the scalar multiplier and the number of the row and multiplies all elements in that row.
    def scalarTimesRow(self, num, row_num):
        real_number = int(float(num))
        row_number = (row_num - 1)

        newMatrix = MatrixMaster(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                newMatrix.data[i][j] = self.data[i][j]
                newMatrix.data[row_number][j] = self.data[row_number][j] * real_number
        return newMatrix

# Row switching. Switches two rows of a matrix.
    def switchRows(self, row_one_num, row_two_num):
        row1_num = row_one_num - 1
        row2_num = row_two_num - 1

        newMatrix = MatrixMaster(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                newMatrix.data[i][j] = self.data[i][j]
                newMatrix.data[row1_num][j] = self.data[row1_num][j]

            
# Example usage
if __name__ == "__main__":
    trixie = MatrixMaster(2, 3)
    trixie.data = [[1, 2, 3], 
                   [4, 5, 6]]
    alice = MatrixMaster(3, 2)
    alice.data = [[7, 8], 
                  [9, 10], 
                  [11, 12]]

    #trixie.print_matrix()
    #trixie.plus(alice).print_matrix()
    #trixie.times(alice).print_matrix()
    #trixie.scalarTimesRow(2.0, 2).print_matrix()
    #trixie.switchRows(1, 2).print_matrix()

    

