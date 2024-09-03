import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
iris = load_iris()
data = iris.data
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data)
U, S, VT = np.linalg.svd(data_standardized)

print("Original Matrix (First 5 Rows):")
print(data_standardized[:5])
print("\nLeft Singular Vectors (U, first 5 rows):")
print(U[:5])
print("\nSingular Values (S):")
print(S)
print("\nRight Singular Vectors (V^T):")
print(VT)
