import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Customer data
data = {
    "Customer": ["A", "B", "C", "D", "E",
                 "F", "G", "H", "I", "J"],

    "Annual_Income": [25, 27, 30, 32, 35,
                      70, 75, 80, 85, 90],

    "Spending_Score": [80, 75, 85, 70, 78,
                       30, 25, 35, 20, 28]
}

df = pd.DataFrame(data)

# Select features
X = df[["Annual_Income", "Spending_Score"]]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

# Create clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Calculate silhouette score
score = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print("Customer Segmentation:")
print(df)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

print("\nInertia:")
print(kmeans.inertia_)

print("\nSilhouette Score:")
print(score)

# Display customers in each cluster
for cluster in sorted(df["Cluster"].unique()):
    print(f"\nCluster {cluster}:")
    print(df[df["Cluster"] == cluster])
