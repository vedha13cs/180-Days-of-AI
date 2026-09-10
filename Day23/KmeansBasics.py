import numpy as np
from sklearn.cluster import KMeans

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

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
kmeans.fit(X)

# Cluster labels
print("Cluster Labels:")
print(kmeans.labels_)

# Cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Inertia
print("\nInertia:")
print(kmeans.inertia_)

# Predict clusters for new data
new_data = np.array([
    [2, 3],
    [9, 9],
    [20, 20]
])

predictions = kmeans.predict(new_data)

print("\nPredicted Clusters:")
print(predictions)
