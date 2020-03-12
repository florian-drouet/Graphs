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
    random_graph = random_graph().make_random_vertices(6,10).make_edges().make_coordinates()
    #plotly_visualization(random_graph)
    kruskal_result = kruskal(random_graph.edges, list(random_graph.vertices.keys()))
    #plotly_visualization(random_graph, kruskal_edges=kruskal_result[0])
    print("Minimum spanning tree cost is : ",kruskal_result[1])

    
    #Not_random
    vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2))
    graph = graph()
    graph.make_vertices(vertices_list)
    graph.make_edges()
    graph.make_coordinates()
    kruskal_edges = kruskal(graph.edges, list(graph.vertices.keys()))[0]
    plotly_visualization(graph)
    #plotly_visualization(graph, kruskal_edges=kruskal_edges)
    #plt.scatter(graph.x_coordinates, graph.y_coordinates)
    #plt.show()