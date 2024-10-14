"""
Ivar Eftedal
ivar.odegardstuen.eftedal@nmbu.no

Jørgen Asmundvaag
jorgen.asmundvaag@nmbu.no
"""

import numpy as np

SIZE = 5_000

"""
Task 1:
"""

# Create the matrix using numpy:
arr = np.random.randint(100, size=(SIZE, SIZE))

# Prep the matrix for more optimized performance:
matrix_1d = [item for row in arr for item in row]
len_matrix_1d = len(matrix_1d)


def sum_matrix(matrix: list) -> int:
    total = 0
    for item in matrix:
        total += item
    return total


def mean_matrix(len_matrix: int, total: int) -> float:
    return total / len_matrix


def variance_matrix(matrix: list, mean: float, len_matrix: int) -> float:
    diff_squared = [(x - mean) ** 2 for x in matrix]
    variance = sum(diff_squared) / len_matrix

    return variance


def multiply_matrix(matrix: np.array, multiplier: int) -> np.array:
    return matrix * multiplier


total = sum_matrix(matrix_1d)
mean = mean_matrix(len_matrix_1d, total)
variance = variance_matrix(matrix_1d, mean, len_matrix_1d)
matrix_times_multiplier = multiply_matrix(arr, 2)


print(f"Mean of matrix: {mean}")
print(f"Variance of matrix: {variance}")
print(f"Sum of matrix: {total}")
print(f"Matrix times multiplier: \n{matrix_times_multiplier}")


"""
Task 2:
"""

# Initiate matrix
matrix = np.zeros((50, 50))

# Make the content of the matrix the desired content
for i in range(50):
    matrix[i, i] = -2

    if i > 0:
        matrix[i, i - 1] = 1
    if i < 50 - 1:
        matrix[i, i + 1] = 1


def power_iteration(matrix, num_iterations=100):
    v = np.random.rand(matrix.shape[0])

    # Power iteration
    for _ in range(num_iterations):
        # Matrix-vector multiplication
        v_new = np.dot(matrix, v)

        # Normalize the new vector
        v_new_norm = np.linalg.norm(v_new)
        v = v_new / v_new_norm

    # After 100 iterations, return the approximate dominant eigenvalue
    dominant_eigenvalue = np.dot(np.dot(matrix, v), v) / np.dot(v, v)

    return dominant_eigenvalue


# Compute the dominant eigenvalue using power iteration
dominant_eigenvalue = power_iteration(matrix)
print("Dominant eigenvalue (approximation):", dominant_eigenvalue)

# Check the result by computing the eigenvalues using numpys function
eigenvalues, eigenvectors = np.linalg.eig(matrix)
abs_eigenvalues = np.abs(eigenvalues)
dominant_index = np.argmax(abs_eigenvalues)
print("Dominant eigenvalue (numpy):", eigenvalues[dominant_index])
