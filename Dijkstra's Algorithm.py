import heapq
def dijkstra(adj_matrix, start):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    previous = [None] * n
    priority_queue = [(0, start)]  # (distance, node)
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if visited[current_node]:
            continue
        visited[current_node] = True
        for neighbor in range(n):
            weight = adj_matrix[current_node][neighbor]
            if weight > 0 and not visited[neighbor]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    return distances, previous
adj_matrix = [
    [0, 6, 0, 1, 0],
    [6, 0, 5, 2, 2],
    [0, 5, 0, 0, 5],
    [1, 2, 0, 0, 1],
    [0, 2, 5, 1, 0]
]
start_node = 0  
distances, previous = dijkstra(adj_matrix, start_node)
print("Shortest distances from node", start_node, ":", distances)
