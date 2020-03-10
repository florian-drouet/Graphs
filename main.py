from matplotlib import pyplot as plt

graph = edges()
graph.make_vertices(50,1000)
graph.make_edges()
graph.make_coordinates()
plt.scatter(graph.x_coordinates, graph.y_coordinates)
plt.show()
