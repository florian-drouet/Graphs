import plotly.graph_objects as go

def plotly_visualization(graph, kruskal_edges = None):

    edge_x = []
    edge_y = []
    vertice_x = []
    vertice_y = []

    if kruskal_edges == None:
        edges = graph.edges
    else:
        edges = kruskal_edges

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