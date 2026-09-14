import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Sample dataset
X = np.array([
    [10, 20, 30, 40],
    [12, 22, 32, 42],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [22, 32, 42, 52],
    [25, 35, 45, 55]
])

print("Original Shape:")
print(X.shape)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

print("\nReduced Shape:")
print(X_reduced.shape)

print("\nReduced Data:")
print(X_reduced)

# Explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Explained Variance:")
print(pca.explained_variance_ratio_.sum())
