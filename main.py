from matplotlib import pyplot as plt
from graph_classes.random_undirected_graph import random_graph
from graph_classes.undirected_graph import graph
from graph_classes.directed_graph import digraph
from plotly_graphs import plotly_visualization
from graph_algorithms.kruskal import kruskal
from graph_algorithms.dijkstra import dijkstra


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
    #random_graph = random_graph().make_graph(25,100)
    #plotly_visualization(random_graph)
    #kruskal_vertices_list = kruskal(random_graph.edges, list(random_graph.vertices.keys()))
    #plotly_visualization(random_graph, vertices_list=kruskal_vertices_list[0])
    #print("Minimum spanning tree cost is : ",kruskal_vertices_list[1])
    
    #Not_random
    #vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2))
    #vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2), (3,5), (2,2), (6,8), (0,7))
    #vertices_list = ((0,0), (2,2), (2,5), (4,0)) #for medium article
    #graph = graph().make_graph(vertices_list)
    #plotly_visualization(graph)
    #plotly_visualization(graph, vertices_list=kruskal(graph.edges, list(graph.vertices.keys()))[0])

    vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2), (3,5), (2,2), (6,8), (0,7))
    successors = {0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [1, 8], 5: [8], 6: [4, 9], 7: [9], 8: [9], 9: []}
    digraph = digraph().make_graph(vertices_list, successors)
    #print(digraph.edges)
    #plotly_visualization(digraph)
    dijkstra_predecessors = dijkstra(digraph).dijkstra_algorithm(initial_point=0)
    print(dijkstra_predecessors)
    digraph_dijkstra = digraph.make_graph_from_predecessor(vertices_list, dijkstra_predecessors)
    print(digraph_dijkstra.edges)