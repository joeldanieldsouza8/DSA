class Graph:
    def __init__(self):
        self.adj_list: dict[str, list[str]] = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex: str):
        # Check if the vertex doesn't already exist in the graph
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = [] # Initialise the vertex with an empty list to represent no edges with other vertices
            return True

        return False


my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()

"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""
