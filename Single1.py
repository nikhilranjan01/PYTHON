import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data)
U, S, VT = np.linalg.svd(data_standardized)
svd_2d = U[:, :2]
plt.figure(figsize=(8, 6))

colors = ['r', 'g', 'b']
for i, color, label in zip(range(len(target_names)), colors, target_names):
    plt.scatter(svd_2d[target == i, 0], svd_2d[target == i, 1], color=color, label=label)

plt.title('Iris Dataset Projected onto First Two Principal Components')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True)
plt.show()
