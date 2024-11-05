def k_means(data, k, max_iterations):
    centroids = data[:k]
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in data:
            closest_centroid = min(range(k), key=lambda i: sum((px - cx) ** 2 for px, cx in zip(point, centroids[i]))) 
            clusters[closest_centroid].append(point)
 
        new_centroids = [([sum(dim) / len(cluster) for dim in zip(*cluster)] if cluster else centroids[i]) for i, cluster in enumerate(clusters)]
        
        if centroids == new_centroids:
            break
        centroids = new_centroids
    return clusters
 
data = [list(map(float, input("Enter point coordinates (space-separated): ").split())) for _ in range(int(input("Enter number of data points: ")))]
k = int(input("Enter number of clusters: "))
max_iterations = int(input("Enter max iterations: "))
 
clusters = k_means(data, k, max_iterations)
print("Clusters:", clusters)
