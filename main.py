from matplotlib import pyplot as plt
from graph import graph
from plotly_graphs import plotly_visualization
from kruskal import kruskal

if __name__ == "__main__":
    #random_graph = graph()
    #random_graph.make_random_vertices(50,1000)
    #random_graph.make_edges()
    #random_graph.make_coordinates()
    #plt.scatter(random_graph.x_coordinates, random_graph.y_coordinates)

    vertices_list = ((1,2), (2,5), (3,4), (3,3), (0,1), (4,2))
    graph = graph()
    graph.make_vertices(vertices_list)
    graph.make_edges()
    graph.make_coordinates()
    kruskal_edges = kruskal(graph.edges, list(graph.vertices.keys()))[0]
    print(kruskal_edges)
    plotly_visualization(graph, kruskal_edges=kruskal_edges)
    #plt.scatter(graph.x_coordinates, graph.y_coordinates)
    #plt.show()