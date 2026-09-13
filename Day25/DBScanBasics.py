import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Sample data
X = np.array([
    [1, 2],
    [1, 3],
    [2, 2],
    [2, 3],

    [8, 8],
    [8, 9],
    [9, 8],
    [9, 9],

    [20, 20]   # Possible noise
])

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create DBSCAN model
dbscan = DBSCAN(
    eps=0.6,
    min_samples=3
)

# Find clusters
labels = dbscan.fit_predict(X_scaled)

print("Data:")
print(X)

print("\nCluster Labels:")
print(labels)

# Display clusters
for cluster in sorted(set(labels)):
    if cluster == -1:
        print("\nNoise Points:")
        print(X[labels == cluster])
    else:
        print(f"\nCluster {cluster}:")
        print(X[labels == cluster])
