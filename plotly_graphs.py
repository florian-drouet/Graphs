import plotly.graph_objects as go

def plotly_visualization(graph, vertices_list = None):
    """
    Inputs :
        - a graph object from the class "graph" or "random-graph"
        - (Optional) - a tuple of vertices coordinates in this format : (x_coordinate, y_coordinate)

    This function is used to plot graphs using the python library Plotly. Each vertice is represented as a red dot
    and each edge as a line between two vertices.
    """

    edge_x = []
    edge_y = []
    vertice_x = []
    vertice_y = []

    if vertices_list == None:
        edges = graph.edges
    else:
        edges = vertices_list

    for edge in edges:
        edge_x.append(graph.x_coordinates[edge[0]])
        edge_x.append(graph.x_coordinates[edge[1]])
        edge_x.append(None)
        edge_y.append(graph.y_coordinates[edge[0]])
        edge_y.append(graph.y_coordinates[edge[1]])
        edge_y.append(None)
        
    for vertice in graph.vertices.keys():
        vertice_x.append(graph.x_coordinates[vertice])
        vertice_y.append(graph.y_coordinates[vertice])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_trace = go.Scatter(
        x=vertice_x, y=vertice_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(size=10, line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
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