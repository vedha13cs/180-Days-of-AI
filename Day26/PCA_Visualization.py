import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reduce 4 dimensions to 2
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print("Original Shape:")
print(X.shape)

print("\nReduced Shape:")
print(X_pca.shape)

print("\nExplained Variance:")
print(pca.explained_variance_ratio_)

# Plot PCA result
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Dataset - PCA Visualization")

plt.show()
