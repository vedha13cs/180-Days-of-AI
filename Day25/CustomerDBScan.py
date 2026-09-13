import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

# Customer dataset
data = {
    "Customer": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],

    "Annual_Income": [
        25, 27, 30, 32, 35,
        70, 75, 80, 85, 90
    ],

    "Spending_Score": [
        80, 75, 85, 70, 78,
        30, 25, 35, 20, 28
    ]
}

df = pd.DataFrame(data)

# Select features
X = df[
    ["Annual_Income", "Spending_Score"]
]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
model = DBSCAN(
    eps=0.8,
    min_samples=2
)

df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Segmentation:")
print(df)

# Count clusters
clusters = set(df["Cluster"])

print("\nClusters Found:")
print(clusters)

# Display noise
noise = df[df["Cluster"] == -1]

print("\nNoise Points:")
print(noise)

# Calculate silhouette score only if
# there are at least 2 non-noise clusters
non_noise = df[df["Cluster"] != -1]

if len(set(non_noise["Cluster"])) >= 2:
    score = silhouette_score(
        X_scaled[df["Cluster"] != -1],
        non_noise["Cluster"]
    )

    print("\nSilhouette Score:")
    print(score)
else:
    print("\nSilhouette Score:")
    print("Not enough clusters to calculate it.")
