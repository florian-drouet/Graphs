import numpy as np
from graph_classes.undirected_graph import graph

class digraph(graph):

    def __init__(self):
        super().__init__()

    def make_graph(self, vertices_list, successors):
        self.number_of_vertices = len(vertices_list)
        for i in range(0,self.number_of_vertices):
            self.vertices[i] = vertices_list[i]
            self.successors[i] = []
        self.make_edges(successors)
        self.make_adjacency_matrix(successors)
        self.make_coordinates()
        return self

    def make_edges(self, successors):
        for vertice_1 in self.vertices.keys():
            for vertice in successors[vertice_1]:
                coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                coordinate_x2 = list(self.vertices.values())[vertice][0]
                coordinate_y2 = list(self.vertices.values())[vertice][1]
                euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                self.edges.append([vertice_1,vertice,euclidean_distance])
        self.number_of_edges = len(self.edges)

    def make_adjacency_matrix(self, successors):
        self.adjacency_matrix = np.zeros((self.number_of_vertices,self.number_of_vertices))
        for vertice_1 in self.vertices.keys():
            for vertice in successors[vertice_1]:
                coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                coordinate_x2 = list(self.vertices.values())[vertice][0]
                coordinate_y2 = list(self.vertices.values())[vertice][1]
                euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                self.adjacency_matrix[vertice_1,vertice] = euclidean_distance
                self.successors[vertice_1].append(vertice)
