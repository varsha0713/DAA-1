def multistage_graph(graph, cost_matrix):
    num_stages = len(graph)
    num_nodes = len(graph[0])

    
    min_cost = [0] * num_nodes
    path = [-1] * num_stages

   
    for stage in range(num_stages - 2, -1, -1):
        for node in range(num_nodes):
            min_cost[node] = float('inf')
            for neighbor in graph[stage][node]:
                total_cost = cost_matrix[stage][node] + min_cost[neighbor]
                if total_cost < min_cost[node]:
                    min_cost[node] = total_cost
                    path[node] = neighbor

  
    optimal_path = []
    current_node = path[0]
    optimal_path.append(current_node)
    for stage in range(1, num_stages - 1):
        current_node = path[current_node]
        optimal_path.append(current_node)

    return optimal_path[::-1], min_cost[0]


graph = [
    [1, 2],
    [3, 4],
    [5],
    [5],
    []
]

cost_matrix = [
    [2, 1],
    [3, 2],
    [1],
    [3],
    []
]

optimal_path, min_cost = multistage_graph(graph, cost_matrix)
print("Optimal Path:", optimal_path)
print("Min Cost:", min_cost)


//OUTPUT:Optimal Path: [0, 1, 3, 4, 5]
Min Cost: 6
//
