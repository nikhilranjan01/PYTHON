import numpy as np
from sklearn.preprocessing import MinMaxScaler

class LVQ:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.prototypes = None
        self.labels = None

    def initialize_prototypes(self, X, y):
        classes = np.unique(y)
        self.prototypes = np.array([X[y == c][0] for c in classes])
        self.labels = classes

    def update_prototypes(self, x, y):
        closest_idx = np.argmin(np.linalg.norm(self.prototypes - x, axis=1))
        if self.labels[closest_idx] == y:
            self.prototypes[closest_idx] += self.learning_rate * (x - self.prototypes[closest_idx])
        else:
            self.prototypes[closest_idx] -= self.learning_rate * (x - self.prototypes[closest_idx])

    def fit(self, X, y):
        self.initialize_prototypes(X, y)
        for epoch in range(self.epochs):
            for i in range(len(X)):
                self.update_prototypes(X[i], y[i])

    def predict(self, X):
        predictions = []
        for x in X:
            closest_idx = np.argmin(np.linalg.norm(self.prototypes - x, axis=1))
            predictions.append(self.labels[closest_idx])
        return np.array(predictions)

if __name__ == "__main__":
    X = np.array([[1, 1], [2, 2], [3, 3], [8, 8], [9, 9], [10, 10]])
    y = np.array([0, 0, 0, 1, 1, 1])
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    lvq = LVQ(learning_rate=0.1, epochs=10)
    lvq.fit(X_scaled, y)
    while True:
        user_input = input("Enter two feature values separated by a comma (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            features = np.array([float(x) for x in user_input.split(",")])
            features_scaled = scaler.transform([features])
            prediction = lvq.predict(features_scaled)
            print(f"Predicted class: {prediction[0]}")
        except Exception as e:
            print(f"Error: {e}. Please try again.")
