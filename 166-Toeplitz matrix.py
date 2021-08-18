#Function to determine if a given matrix is a Toeplitz or not
def Toeplitz(matrix):
    # along the row
    for i in range(len(matrix) - 1):
        # along the column
        for j in range(len(matrix[0]) - 1):
            # comapare current and diagonal element
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True
 
if __name__ == '__main__':
    matrix1 = [[1, 2, 3, 4, 5],
               [0, 1, 2, 3, 4],
               [9, 0, 1, 2, 3]]

    matrix2 = [[2, 3, 5, 7, 9],
               [1, 2, 0, 5, 7],
               [0, 1, 0, 3, 5],
               [4, 0, 1, 2, 3]]
    matrices = [matrix1, matrix2]

    for matrix in matrices:
        if Toeplitz(matrix):
            print("The matrix is Toeplitz.")
        else:
            print("The matrix is not Toeplitz.")

# --------
# Result:
# ----------------------------------------------------------
# The matrix is Toeplitz.
# The matrix is not Toeplitz.
# ----------------------------------------------------------