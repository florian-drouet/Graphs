import numpy as np
import random

class graph:
    
    def __init__(self):
        self.vertices = dict()
        self.number_of_vertices = 0
        self.edges = []
        self.number_of_edges = 0
        self.x_coordinates = []
        self.y_coordinates = []
        
    def make_random_vertices(self, n, rate):
        self.number_of_vertices = n
        for i in range(0,n):
            self.vertices[i] = (random.randint(0,rate*n), random.randint(0,rate*n))
    
    def make_vertices(self, vertices_list):
        self.number_of_vertices = len(vertices_list)
        for i in range(0,self.number_of_vertices):
            self.vertices[i] = vertices_list[i]
        
    def make_edges(self):
        for vertice_1 in self.vertices.keys():
            for vertice_2 in self.vertices.keys():
                if vertice_1 != vertice_2:
                    coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                    coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                    coordinate_x2 = list(self.vertices.values())[vertice_2][0]
                    coordinate_y2 = list(self.vertices.values())[vertice_2][1]
                    euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                    self.edges.append([vertice_1,vertice_2,euclidean_distance])
    
    def make_coordinates(self):
        for vertice in self.vertices.keys():
            self.x_coordinates.append(list(self.vertices.values())[vertice][0])
            self.y_coordinates.append(list(self.vertices.values())[vertice][1])
