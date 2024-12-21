class Graph:
    def __init__(self):
        self.adj_list: dict[str, list[str]] = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, vertex_1: str, vertex_2: str):
        # Check if both vertices are present in the graph
        if vertex_1 and vertex_2 in self.adj_list:
            # Remove 'vertex_1' from 'vertex_2' adjacency list (if it exists)
            if vertex_1 in self.adj_list[vertex_2]:
                self.adj_list[vertex_2].remove(vertex_1)

            # Remove 'vertex_2' from 'vertex_1' adjacency list (if it exists)
            if vertex_2 in self.adj_list[vertex_1]:
                self.adj_list[vertex_1].remove(vertex_2)

            return True

        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

print('Graph before remove_edge():')
my_graph.print_graph()

my_graph.remove_edge('A', 'C')

print('\nGraph after remove_edge():')
my_graph.print_graph()

"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_edge():
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['B', 'A']

    Graph after remove_edge():
    A : ['B']
    B : ['A', 'C']
    C : ['B']

"""
