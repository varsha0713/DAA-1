def hamiltonian_cycle(graph, current_vertex, visited, path, start_vertex):
    if len(path) == len(graph):
        if start_vertex in graph[current_vertex]:
            path.append(start_vertex)
            return True
        return False

    for neighbor in graph[current_vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

            if hamiltonian_cycle(graph, neighbor, visited, path, start_vertex):
                return True

            path.pop()
            visited[neighbor] = False

    return False

def find_hamiltonian_cycle(graph):
    num_vertices = len(graph)
    for vertex in range(num_vertices):
        visited = [False] * num_vertices
        visited[vertex] = True
        path = [vertex]

        if hamiltonian_cycle(graph, vertex, visited, path, vertex):
            return path

    return []

# Example graph
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}

cycle = find_hamiltonian_cycle(graph)
if cycle:
    print("Hamiltonian Cycle:", cycle)
else:
    print("No Hamiltonian Cycle found.")

