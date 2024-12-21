class Graph:
    def __init__(self):
        self.adj_list: dict[int, list[int]] = {}

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

    def add_edge(self, vertex_1: int, vertex_2: int):
        # Before adding an edge, check if both vertices exist in the adjacency list
        if vertex_1 and vertex_2 not in self.adj_list:
            return False

        self.adj_list[vertex_1].append(vertex_2)
        self.adj_list[vertex_2].append(vertex_1)
        return True


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()

"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""
