from matplotlib import pyplot as plt
from graph_classes.random_undirected_graph import random_graph
from graph_classes.undirected_graph import graph
from plotly_graphs import plotly_visualization
from graph_algorithms.kruskal import kruskal

if __name__ == "__main__":
    
    '''
    First step : random graph creation
        We create a random graph of 6 vertices and a ratio of 10.
        We create edges and x and y coordinates for this graph.
    Second step : displaying random graph
        We display the graph with the plotly visualization
    Third step : applying kruskal's algorithm to get the minimum spanning tree of the graph
        We apply kruskal's algorithms to the graph to get the edges and the total cost
        We plot the obtained minimal spanning tree
    '''
    
    #Random graph
    random_graph = random_graph().make_random_graph(5,1)
    print("The number of vertices is :", random_graph.number_of_vertices)
    print("The number of edges is :", random_graph.number_of_edges)
    print("The edges are :\n", random_graph.edges)
    print("The adjacency matrix is :\n", random_graph.adjacency_matrix)
    #plotly_visualization(random_graph)
    #kruskal_vertices_list = kruskal(random_graph.edges, list(random_graph.vertices.keys()))
    #plotly_visualization(random_graph, vertices_list=kruskal_vertices_list[0])
    #print("Minimum spanning tree cost is : ",kruskal_vertices_list[1])
    
    #Not_random
    vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2))
    #vertices_list = ((0,0), (2,2), (2,5), (4,0)) for medium article
    graph = graph().make_graph(vertices_list)
    print(graph.adjacency_matrix)
    #print(graph.adjacency_matrix)
    #print(graph.x_coordinates)
    #print(graph.y_coordinates)
    print(graph.edges)
    plotly_visualization(graph)
    plotly_visualization(graph, vertices_list=kruskal(graph.edges, list(graph.vertices.keys()))[0])