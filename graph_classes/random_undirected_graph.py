import numpy as np
import random
from graph_classes.undirected_graph import graph

class random_graph(graph):
    """
    This class implements an undirected random graph, it is inherited from "graph" class in undirected_graph.py

    Attributes :
        n : the number of vertices you want to display
        rate : a "ratio" number, the greater it is, the larger the graph will be (used in make_random_vertices)
    """

    def __init__(self):
        super().__init__()
        
    def make_graph(self, n, rate):
        """Performs the creation of a random graph. Each coordinates of a vertice are randomly created and then scaled with "rate"."""
        self.number_of_vertices = n
        for i in range(0,n):
            self.vertices[i] = (random.randint(0,rate*n), random.randint(0,rate*n))
            self.successors[i] = []
        #if a graph has vertices with same coordinates then we recreate a new graph
        if self.check_vertices() == True:
            self.make_graph(n, rate)
        self.make_edges()
        self.make_adjacency_matrix()
        self.make_coordinates()
        return self

    def check_vertices(self):
        """
        Checks if vertices coordinates are unique in vertices dictionnary.
        When graph are randomly made, there is always a probability that two vertices are created at the same coordinates.
        This function return "True" if it finds two vertices at the same coordinates. To reduce the chance of two vertices
        at the same coordinates you can also play with "rate" attribute since it increases the size of the graph.
        """
        check_bool = len(self.vertices) != len(set(self.vertices.values()))
        return check_bool
