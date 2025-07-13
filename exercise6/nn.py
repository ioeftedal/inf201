import numpy as np


class SingleLayerPerceptron:
    def __init__(self, input_size) -> None:
        # Initialization of weights and bias with random values
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand(1)

    def sigmoid(self, x) -> float:
        # Funzione di attivazione Sigmoid
        return 1 / (1 + np.exp(-x))

    def predict(self, inputs):
        # Calculation of the weighted sum of the inputs and application of the activation function
        z = np.dot(inputs, self.weights) + self.bias
        return self.sigmoid(z)


if __name__ == "__main__":
    # Creazione di un perceptron con 3 input
    input_size = 3
    perceptron = SingleLayerPerceptron(input_size)

    # Input example
    input_data = np.array([0.5, 0.3, 0.8])

    # Output prediction
    output = perceptron.predict(input_data)

    # Print the results
    print("Input:", input_data)
    print("Output:", output)
