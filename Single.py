import numpy as np

# Generate a random dataset (for example, 5x3 matrix)
np.random.seed(0)  # Seed for reproducibility
data = np.random.rand(5, 3)

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(data)

# Display the results
print("Original Matrix (Data):")
print(data)
print("\nLeft Singular Vectors (U):")
print(U)
print("\nSingular Values (S):")
print(S)
print("\nRight Singular Vectors (V^T):")
print(VT)
