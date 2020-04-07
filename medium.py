import numpy as np

class complete_graph:
    """
    This class implements an undirected graph.
    Attributes :
        vertices_list : a tuple of vertices coordinates in this format : (x_coordinate, y_coordinate)
    """        
    def __init__(self):
        """
        Initialize graphs :
            vertices as a dictionnary {vertice_0 : (x_coordinate_vertice_0, y_coordinate_vertice_0), ...}
            number_of_vertices as integer
            edges as a list in which each element is a list like : [vertice_1, vertice_2, euclidean distance between the vertices]
            number of edges as a integer
        """
        self.vertices = dict()
        self.number_of_vertices = 0
        self.edges = []
        self.number_of_edges = 0
    

    def make_edges(self):
        """Performs creation of edges in the form : [vertice_1, vertice_2, euclidean distance between the two vertices]"""
        for vertice_1 in self.vertices.keys():
            for vertice_2 in self.vertices.keys():
                if vertice_1 != vertice_2 and vertice_1 < vertice_2:
                    coordinate_x1 = list(self.vertices.values())[vertice_1][0]
                    coordinate_y1 = list(self.vertices.values())[vertice_1][1]
                    coordinate_x2 = list(self.vertices.values())[vertice_2][0]
                    coordinate_y2 = list(self.vertices.values())[vertice_2][1]
                    euclidean_distance = int(np.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2))
                    self.edges.append([vertice_1,vertice_2,euclidean_distance])
        self.number_of_edges = len(self.edges)

    def make_graph(self, vertices_list):
        """Performs the creation of a graph from vertices_list (vertices+edges+coordinates)"""
        self.number_of_vertices = len(vertices_list)
        for i in range(0,self.number_of_vertices):
            self.vertices[i] = vertices_list[i]
        self.make_edges()
        return self

if __name__ == "__main__":
    vertices_list = ((0,0), (2,2), (2,5), (4,0))
    print("The list of vertices is : ",vertices_list,"\n")

    #We initialize an empty graph
    graph = complete_graph()
    #We create a complete graph from vertices_list
    graph.make_graph(vertices_list)

    print("We created a complete graph with",graph.number_of_vertices,"vertices.\nThe dictionnary 'vertices' is :",graph.vertices,"\n")
    print("A total of",graph.number_of_edges,"vertices has been created and the total list of edges is :\n", graph.edges)