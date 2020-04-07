import copy
import numpy as np
from graph_classes.undirected_graph import graph

class dijkstra(graph):

    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.set_of_vertices = []
        self.set = []
        self.opposite_set = []
        self.costs = dict()
        self.predecessors = dict()

    def initialize_sets(self, initial_point):
        self.set_of_vertices = list(self.graph.vertices.keys())
        self.set = [initial_point]
        
        for i in range(0, np.shape(self.graph.adjacency_matrix)[0]):
            if i == initial_point:
                self.costs[i] = [0]
                self.predecessors[i] = [initial_point]
            else :
                self.costs[i] = [1000]
                self.predecessors[i] = []
                self.opposite_set.append(i)

        for k in self.graph.successors[initial_point]:
            self.costs[k].append(self.graph.adjacency_matrix[initial_point,k])
            self.predecessors[k].append(initial_point)
            if len(self.predecessors[k]) >= 2:
                self.predecessors[k] = [np.int(self.predecessors[k][1])]
            if len(self.costs[k]) >= 2:
                self.costs[k] = [np.int(self.costs[k][1])]
        
        return self

    def intersection(self, liste1, liste2):
        liste3 = [value for value in liste1 if value in liste2]
        return liste3

    def dijkstra_algorithm(self, initial_point):
        self.initialize_sets(initial_point)
        while (list(np.sort(self.set)) != self.set_of_vertices):
            liste_temp = []
            for j in self.opposite_set:
                liste_temp.append(self.costs[j][0])
                temp = np.argmin(liste_temp)
                ind_min = self.opposite_set[temp]
            self.set.append(ind_min)
            self.opposite_set.remove(ind_min)
            for j in self.intersection(self.graph.successors[ind_min], self.opposite_set):
                if self.costs[ind_min][0] + self.graph.adjacency_matrix[ind_min,j] < self.costs[j][0]:
                    self.costs[j][0] = self.costs[ind_min][0] + self.graph.adjacency_matrix[ind_min,j]
                    self.predecessors[j].append(ind_min)
                    if len(self.predecessors[j]) >= 2:
                        self.predecessors[j] = [self.predecessors[j][1]]
        return self.predecessors