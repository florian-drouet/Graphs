import numpy as np
import random

class graph:
    """
    This class implements an undirected (not-random) graph.

    Attributes :
        vertices_list : a tuple of vertices coordinates in this format : (x_coordinate, y_coordinate)
    """
        
    def __init__(self):
        """
        Inits graph
            vertices as a dictionnary {vertice_0 : (x_coordinate_vertice_0, y_coordinate_vertice_0), ...}
            number_of_vertices as integer
            edges as a list in which each element is a list like :
                [vertice_1, vertice_2, euclidean distance between the two vertices]
            number of edges as a integer
            x_coordinates as a list (contains all the x_vertices' coordinates) - used for plotting graphs in plotly_visualization
            y_coordinates as a list (contains all the y_vertices' coordinates) - used for plotting graphs in plotly_visualization
            adjacency_matrix as a squared matrix of dimension the number of vertices
        """
        self.vertices = dict()
        self.number_of_vertices = 0
        self.edges = []
        self.number_of_edges = 0
        self.x_coordinates = []
        self.y_coordinates = []
        self.adjacency_matrix = []
        self.successors = dict()
        
    def make_graph(self, vertices_list):
        """Performs the creation of a graph from vertices_list (vertices+edges+coordinates)"""
        self.number_of_vertices = len(vertices_list)
        for i in range(0,self.number_of_vertices):
            self.vertices[i] = vertices_list[i]
            self.successors[i] = []
        self.make_edges()
        self.make_adjacency_matrix()
        self.make_coordinates()
        return self
        
    def make_edges(self):
        """Performs creation of edges (as specified in __init__ doc)"""
        for vertice_1 in self.vertices.keys():
            for vertice_2 in self.vertices.keys():
                if vertice_1 != vertice_2:
                    coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                    coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                    coordinate_x2 = list(self.vertices.values())[vertice_2][0]
                    coordinate_y2 = list(self.vertices.values())[vertice_2][1]
                    euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                    self.edges.append([vertice_1,vertice_2,euclidean_distance])
        self.number_of_edges = len(self.edges)
    
    def make_adjacency_matrix(self):
        """Performs creation of adjacency matrix (as specified in __init__ doc)"""
        self.adjacency_matrix = np.zeros((self.number_of_vertices,self.number_of_vertices))
        for vertice_1 in self.vertices.keys():
            for vertice_2 in self.vertices.keys():
                if vertice_1 != vertice_2:
                    coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                    coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                    coordinate_x2 = list(self.vertices.values())[vertice_2][0]
                    coordinate_y2 = list(self.vertices.values())[vertice_2][1]
                    euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                    self.adjacency_matrix[vertice_1,vertice_2] = euclidean_distance
                    self.successors[vertice_1].append(vertice_2)

    def make_coordinates(self):
        """Performs creation of coordinates' lists (as specified in __init__ doc)"""
        for vertice in self.vertices.keys():
            self.x_coordinates.append(list(self.vertices.values())[vertice][0])
            self.y_coordinates.append(list(self.vertices.values())[vertice][1])
