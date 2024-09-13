import numpy as np
def find_closest_cluster(clusters, input_vector):
    distances = [np.linalg.norm(cluster - input_vector) for cluster in clusters]
    return np.argmin(distances)
def update_weights(clusters, cluster_to_update, input_vector, learning_rate):
    for i, cluster in enumerate(clusters):
        if np.all(cluster == cluster_to_update):
            closest_cluster_index = i
            break
    else:
        raise ValueError("Cluster to update not found in clusters")
    clusters[closest_cluster_index] += learning_rate * (input_vector - clusters[closest_cluster_index])
clusters = [np.array([0.2, 0.3]), np.array([0.6, 0.5]), np.array([0.4, 0.7]), np.array([0.9, 0.6]), np.array([0.2, 0.8])]
input_vector = np.array([0.3, 0.4])
learning_rate = 0.3
print("Initial clusters:")
for cluster in clusters:
    print(cluster)
clusters_to_update = [np.array([0.2, 0.3]), np.array([0.6, 0.5])]

for cluster_to_update in clusters_to_update:
    update_weights(clusters, cluster_to_update, input_vector, learning_rate)
print("\nUpdated clusters:")
for cluster in clusters:
    print(cluster)