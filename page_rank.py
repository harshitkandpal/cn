def calculate_page_rank(graph, num_iterations=100, d=0.85):
    # Initialize page rank values
    page_rank = {node: 1 / len(graph) for node in graph}
    
    for _ in range(num_iterations):
        new_rank = {}
        for node in graph:
            new_rank[node] = (1 - d) / len(graph)  # Base rank for each node
            for neighbor in graph[node]:
                new_rank[node] += d * (page_rank[neighbor] / len(graph[neighbor]))
        page_rank = new_rank
    
    return page_rank

# Example usage
if __name__ == "__main__":
    # Define a simple directed graph
    web_graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C'],
    }

    # Calculate PageRank
    ranks = calculate_page_rank(web_graph)
    print("PageRank Scores:", ranks)