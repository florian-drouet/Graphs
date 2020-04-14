from matplotlib import pyplot as plt
from graph_classes.random_undirected_graph import random_graph
from graph_classes.undirected_graph import graph
from plotly_graphs import plotly_visualization
from graph_algorithms.kruskal import kruskal, kruskal_v2
import random
import time
import numpy as np


def kruskal_complexity(n):
    #number_of_edges = (n*(n-1))/2
    return n*np.log10(n)


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
    #random.seed(9999)
    '''
    empirical_complexity = dict()
    theorical_complexity = dict()
    for number_of_vertices in range(0,500):
        print(kruskal_complexity(number_of_vertices))
        theorical_complexity[number_of_vertices] = kruskal_complexity(number_of_vertices)
    random_graph = random_graph()
    for number_of_vertices in range(2,432,30):        
        random_graph.make_random_graph(n=number_of_vertices,rate=1000)
        start = time.time()
        kruskal_vertices_list = kruskal(random_graph.edges, list(random_graph.vertices.keys()))
        end = time.time()
        empirical_complexity[number_of_vertices] = end-start

    print(empirical_complexity)
    plt.scatter(x=list(empirical_complexity.keys()),y=100*list(empirical_complexity.values()))
    plt.plot(list(theorical_complexity.values()))
    plt.show()
    '''
    random_graph = random_graph()
    random_graph.make_random_graph(20,100)
    #print("The number of vertices is :", random_graph.number_of_vertices)
    #print("The number of edges is :", random_graph.number_of_edges)
    #print("The edges are :\n", random_graph.edges)
    #print("The adjacency matrix is :\n", random_graph.adjacency_matrix)
    #plotly_visualization(random_graph)
    #kruskal_vertices_list = kruskal(random_graph.edges, list(random_graph.vertices.keys()))
    #kruskal_vertices_list = kruskal_v2(random_graph.edges, list(random_graph.vertices.keys()))
    #plotly_visualization(random_graph, edges_list=kruskal_vertices_list[0])
    #print("Minimum spanning tree cost is : ",kruskal_vertices_list[1])
    #random_graph.make_random_graph(100,100)
    #plotly_visualization(random_graph)
    
    #Not_random
    #vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2))
    #vertices_list = ((0,0), (2,2), (2,5), (4,0)) #for medium article
    vertices_list = ((0,0), (1,2), (2,1), (3,4), (3,3),
                     (30,0), (34,2), (27,1), (38,6), (31,3),
                     (0,30), (3,27), (4,34), (1,32), (5,27),
                     (30,30), (29,34), (27,30), (36,36), (31,32),
                     (15,15), (12,16), (13,18), (14,14), (12,12))
    graph = graph().make_graph(vertices_list)
    #kruskal_vertices_list = kruskal(graph.edges, list(graph.vertices.keys()),5)[0]
    kruskal_vertices_list = kruskal_v2(graph.edges, list(graph.vertices.keys()))[0]
    #print(graph.adjacency_matrix)
    #print(graph.adjacency_matrix)
    #print(graph.x_coordinates)
    #print(graph.y_coordinates)
    #print(graph.edges)
    #print(graph.number_of_edges)
    #n = graph.number_of_vertices
    #print((n*(n-1)/2))
    #plotly_visualization(graph)
    #print(kruskal(graph.edges, list(graph.vertices.keys()),5)[0])
    #plotly_visualization(graph, edges_list=kruskal(graph.edges, list(graph.vertices.keys()),5)[0])