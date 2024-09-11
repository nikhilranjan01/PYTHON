import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

class SelfOrganizingMap:
    def __init__(self, m, n, dim, learning_rate=0.5, radius=1.0, decay_function=None, num_iterations=10000):
        self.m = m  
        self.n = n  
        self.dim = dim  
        self.learning_rate = learning_rate
        self.radius = radius
        self.decay_function = decay_function if decay_function else self.linear_decay
        self.num_iterations = num_iterations
        self.weights = np.random.rand(m, n, dim)

    def find_bmu(self, x):
        bmu_idx = None
        min_dist = np.inf
        for i in range(self.m):
            for j in range(self.n):
                w = self.weights[i, j]
                dist = np.linalg.norm(x - w)
                if dist < min_dist:
                    min_dist = dist
                    bmu_idx = (i, j)
        
        return bmu_idx

    def update_weights(self, x, bmu_idx, iteration):
        learning_rate = self.decay_function(self.learning_rate, iteration, self.num_iterations)
        radius = self.decay_function(self.radius, iteration, self.num_iterations)
        for i in range(self.m):
            for j in range(self.n):
                dist_to_bmu = np.linalg.norm(np.array([i, j]) - np.array(bmu_idx))
                
                if dist_to_bmu <= radius:
                    influence = np.exp(-dist_to_bmu / (2 * (radius ** 2)))
                    self.weights[i, j] += influence * learning_rate * (x - self.weights[i, j])

    def linear_decay(self, initial_value, iteration, max_iterations):
        return initial_value * (1 - (iteration / max_iterations))

    def train(self, X):
        X = normalize(X)
        for iteration in range(self.num_iterations):
            x = X[np.random.randint(0, len(X))]
            bmu_idx = self.find_bmu(x)
            self.update_weights(x, bmu_idx, iteration)

    def plot_som(self):
        plt.figure(figsize=(10, 10))
        for i in range(self.m):
            for j in range(self.n):
                plt.scatter(self.weights[i, j, 0], self.weights[i, j, 1], color='blue')
        plt.title('Self Organizing Map')
        plt.show()

# Example usage:
if __name__ == "__main__":
    X = np.random.rand(100, 3)  
    som = SelfOrganizingMap(m=10, n=10, dim=3, learning_rate=0.5, radius=3, num_iterations=1000)
    som.train(X)
    som.plot_som()
