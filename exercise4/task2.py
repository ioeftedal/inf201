import time

import numpy as np

SIZE = 10_000


def matrix_vector_product(matrix: list[list], vector: list) -> list:
    y_i = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            y_i[i] += matrix[i][j] * vector[j]

    return y_i


def numpy_matrix_vector_product(matrix: np.array, vector: np.array) -> np.array:
    return matrix.dot(vector)


matrix2, vector2 = np.random.randint(SIZE, size=(SIZE, SIZE)), np.random.randint(
    SIZE, size=SIZE
)

matrix1, vector1 = matrix2.tolist(), vector2.tolist()


start_time1 = time.time()
matrix_vector_product(matrix1, vector1)
stop_time1 = time.time()
print(f"python list: {stop_time1 - start_time1}")

start_time2 = time.time()
numpy_matrix_vector_product(matrix2, vector2)
stop_time2 = time.time()
print(f"Numpy array: {stop_time2 - start_time2}")
