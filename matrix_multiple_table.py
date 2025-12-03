import numpy as np #using numpy as module
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[(6,7,8),(9,10,11)]])

print("Addition:\n",A+B)
print("subtraction:\n", A-B)
print("multiplication:\n",A*B)

def multiply_matrices(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):          # rows of A
        for j in range(len(B[0])):   # columns of B
            for k in range(len(B)):  # columns of A / rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

def multiply_matrices(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):          # rows of A
        for j in range(len(B[0])):   # columns of B
            for k in range(len(B)):  # columns of A / rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]
