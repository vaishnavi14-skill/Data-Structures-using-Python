class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0]*vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def print_matrix(self):
        print("Adjacency Matrix:")
        # Print header row
        print("   ", end="")
        for i in range(self.V):
            print(f"{i} ", end="")
        print()
        for i in range(self.V):
            print(f"{i}: ", end="")
            for j in range(self.V):
                print(f"{self.matrix[i][j]} ", end="")
            print()
    def print_list(self):
        print("Adjacency List:")
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i}: {' '.join(map(str, neighbors))}")
g = Graph(5)
edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]
for u, v in edges:
    g.add_edge(u, v)
g.print_matrix()
print()
g.print_list()
