import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Sample data
X = np.array([
    [1, 2],
    [1, 3],
    [2, 2],
    [8, 8],
    [9, 8],
    [8, 9],
    [20, 20],
    [21, 19],
    [20, 21]
])

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create Agglomerative Clustering model
model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Fit and predict clusters
labels = model.fit_predict(X_scaled)

print("Data Points:")
print(X)

print("\nCluster Labels:")
print(labels)

# Display each cluster
for cluster in sorted(set(labels)):
    print(f"\nCluster {cluster}:")
    print(X[labels == cluster])
