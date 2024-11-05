import numpy as np

num_nodes = 3
iterations = 10
damping_factor = 0.85

adj_matrix = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 0]
])

transition_matrix = adj_matrix / adj_matrix.sum(axis=0)

rank_vector = np.ones(num_nodes) / num_nodes

for i in range(iterations):
    rank_vector = ((1 - damping_factor) / num_nodes) + damping_factor * transition_matrix.dot(rank_vector)
    print(f"Iteration {i+1}: {rank_vector}")

print("\nFinal PageRank:", rank_vector)
