import numpy as np
import plotly.graph_objects as go

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
        self.x_coordinates = []
        self.y_coordinates = []
    

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
        self.make_coordinates()
        return self
    
    def make_coordinates(self):
        """Performs creation of coordinates' lists (as specified in __init__ doc)"""
        for vertice in self.vertices.keys():
            self.x_coordinates.append(list(self.vertices.values())[vertice][0])
            self.y_coordinates.append(list(self.vertices.values())[vertice][1])

def plotly_visualization(graph, edges_list = None):
    """
    Inputs :
        - a graph object from the class "graph" or "random-graph"
        - (Optional) - a list of edges in this format [[vertex_0, vertex_1, euclidean_distance], ...]

    This function is used to plot graphs using the python library Plotly. Each vertex is represented as a red dot
    and each edge as a line between two vertices.
    """

    edge_x = []
    edge_y = []
    vertice_x = []
    vertice_y = []
    vertex_text = []

    if edges_list == None:
        edges = graph.edges
    else:
        edges = edges_list

    #We build x and y edges lists with the x and y coordinates lists from class graph
    for edge in edges:
        edge_x.append(graph.x_coordinates[edge[0]])
        edge_x.append(graph.x_coordinates[edge[1]])
        edge_x.append(None)
        edge_y.append(graph.y_coordinates[edge[0]])
        edge_y.append(graph.y_coordinates[edge[1]])
        edge_y.append(None)

    #We build x and y vertices list with the x and y coordinates lists from class graph    
    for vertice in graph.vertices.keys():
        vertice_x.append(graph.x_coordinates[vertice])
        vertice_y.append(graph.y_coordinates[vertice])

    #We add edges as a scatter plot
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    #We add vertices as a scatter plot
    vertex_trace = go.Scatter(
        x=vertice_x, y=vertice_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(size=10, line_width=2))
    
    #We add a hover information which displays the name of the vertex and its coordinates
    for coord in range(0,len(vertice_x)):
        vertex_text.append('Vertex '+str(coord)+', coordinates ('+str(vertice_x[coord])+','+str(vertice_y[coord])+')')
    vertex_trace.text = vertex_text

    #we create the whole figure
    fig = go.Figure(data=[edge_trace, vertex_trace],
                layout=go.Layout(
                    title='<br>Network graph made with Python',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()

def make_set(parent, vertex):
    '''
    Make_set function attributes "None" value to each vertex in parent dictionnary
    '''
    parent[vertex] = None

def find(parent, vertex):
    '''
    Find function recursively searches for the root of a given vertex
    '''
    if parent[vertex] == None:
        return vertex
    return find(parent, parent[vertex])

def union(parent, vertex1, vertex2):
    '''
    Union function unites two trees under the same root
    '''
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)
    if root1 != root2:
        parent[root2] = root1

def kruskal(edges, vertices, clusters=1):
    '''
    Naive kruskal's algorithm implementation for minimum spanning tree
    '''
    if clusters > len(vertices):
        return print("Error : the number of vertices is inferior to the number of clusters.")
    minimum_spanning_tree = []
    cost = 0
    parent = dict()
    for vertex in vertices:
        make_set(parent, vertex)
    edges_sorted = sorted(edges,key=lambda cost: cost[2])
    for edge in edges_sorted:
        if find(parent, edge[0]) != find(parent, edge[1]):
            union(parent, edge[0], edge[1])
            minimum_spanning_tree.append(edge)
            cost = cost + edge[2]
        if list(parent.values()).count(None) == clusters:
            break
    return minimum_spanning_tree, cost

if __name__ == "__main__":
    vertices_list = ((0,0), (1,2), (2,1), (3,4), (3,3),
                     (30,0), (34,2), (27,1), (38,6), (31,3),
                     (0,30), (3,27), (4,34), (1,32), (5,27),
                     (30,30), (29,34), (27,30), (36,36), (31,32),
                     (15,15), (12,16), (13,18), (14,14), (12,12))
    print("The list of vertices is : ",vertices_list,"\n")

    #We initialize an empty graph
    graph = complete_graph()
    #We create a complete graph from vertices_list
    graph.make_graph(vertices_list)
    #We launch the data visualization of the graph
    plotly_visualization(graph)
    #We apply kruskal's algorithm to the graph
    kruskal_vertices_list = kruskal(graph.edges, list(graph.vertices.keys()), clusters=5)
    #We launch the data visualization of the clustered graph
    plotly_visualization(graph, kruskal_vertices_list[0])
    

    print("We created a complete graph with",graph.number_of_vertices,"vertices.\nThe dictionnary 'vertices' is :",graph.vertices,"\n")
    print("A total of",graph.number_of_edges,"vertices has been created and the total list of edges is :\n", graph.edges)
    print("Edges are :",kruskal_vertices_list[0],"\nTotal cost is :",kruskal_vertices_list[1])