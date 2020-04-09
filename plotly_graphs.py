import plotly.graph_objects as go

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