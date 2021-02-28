# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:28:24 2021

@author: Lorenzo
"""
def genereate_json_for_3d_graph():
    '''
    this function create the json file that is used by plotly to create the figure 
    for the 3d visualization
    OUTPUT: string in the form of a json file
    '''
    
    import pandas as pd
    import networkx as nx
    import json
    import plotly.graph_objs as go
    import plotly

    
    # import data
    df_edges = pd.read_excel("raan_case_study.xlsx", sheet_name = 0)
    df_nodes = pd.read_excel("raan_case_study.xlsx", sheet_name = 1)


    # create graph (create 2 lists dictionary with the edges and with the nodes and their attributes)
    edges_list = [(el[0], el[1], el[2]) for _, el in df_edges.T.items()]
    nodes_list = [(el[0], {'color': el[1], 'label':el[2]}) for _, el in df_nodes.T.items()]

    # create graph
    G = nx.DiGraph()

    # add nodes and edges to graph
    G.add_nodes_from(nodes_list)
    G.add_weighted_edges_from(edges_list)

    # get positions of nodes in 3D plane
    pos = nx.layout.spring_layout(G, dim =3)
    Xn=[pos[el][0] for el in pos] # x-coordinates of nodes
    Yn=[pos[el][1] for el in pos] # y-coordinates
    Zn=[pos[el][2] for el in pos] # z-coordinates




    # creates lists with attributes of nodes
    names_list = [el[1]['label'] for el in G.nodes(data=True)] # labels
    attr_list = [(el[0], el[1]['label']) for el in G.nodes(data=True)] # id and label
    id_list = [el[0] for el in G.nodes(data=True)] # id
    color_list = [el[1]['color'] for el in G.nodes(data=True)] # colors



    # 3D plot of the graph

    # interactive 3D plot
    # create list of position of cones and direction of edges
    # position of the cones
    Xs = [0.55 * pos[el[1]][0] + 0.45 *  pos[el[0]][0] for el in G.edges()]
    Ys = [0.55 * pos[el[1]][1] + 0.45 *  pos[el[0]][1] for el in G.edges()]
    Zs = [0.55 * pos[el[1]][2] + 0.45 *  pos[el[0]][2] for el in G.edges()]
    # direction of the cones
    Us = [pos[el[1]][0] - pos[el[0]][0] for el in G.edges()]
    Vs = [pos[el[1]][1] - pos[el[0]][1] for el in G.edges()]
    Ws = [pos[el[1]][2] - pos[el[0]][2] for el in G.edges()]



    trace1=go.Scatter3d(x=Xn, y=Yn, z=Zn,mode='text+markers', name='nodes', text = id_list,
                            marker=dict(symbol='circle',size=10, color= color_list,
                                        line=dict(color='rgb(50,50,50)', width=0.5)),
                            textposition="bottom center", meta= attr_list, hoverinfo ='text', hovertext = names_list)

    # set axis for plot
    axis=dict(showbackground=False, showline=False, zeroline=False,
                  showgrid=False,
                  showticklabels=True,
                  title='' )

    # set layout for plot
    layout = go.Layout(title="3D visualization (produced with plotly)", width=1000, height=1000, showlegend=False,
                           scene=dict(xaxis=dict(axis), yaxis=dict(axis), zaxis=dict(axis)), margin=dict(t=100),
                           hovermode='closest', annotations=[ dict(showarrow=False, text="", xref='paper',yref='paper',x=0,
                                                                   y=0.1, xanchor='left', yanchor='bottom', font=dict(size=14))],)

    # create figure
    data=[trace1]
    fig=go.Figure(data=data, layout=layout)

    # plotly does not allow to draw directe arrow
    # to show the direction of the edge in the direction of the edge is plotted in the middle of the edge



    # create trace for cones (used to indicate direction of edge)
    # hovering over the edge source and target nodes as well as the
    trace =go.Cone(x=Xs, y=Ys, z=Zs, u=Us, v=Vs,  w=Ws, opacity = 0.4, showscale=False,
                       colorscale=[[0, 'rgb(125,125,125)'], [1,'rgb(125,125,125)']],
                       hoverinfo='text', text=['edge from '+ str(G.nodes(data=True)[e[0]]['label']) + ' ('+
                                      str(e[0])+') '+ ' to ' + str(G.nodes(data=True)[e[1]]['label'])+
                                      ' ('+ str(e[1])  + ') '
                                      ': weight: '+ str (e[2]['weight'])  for e in G.edges(data=True)])
    
    fig.add_trace(trace)

    # get list of weights
    weights_list = [el[2]['weight'] for el in G.edges(data=True)]
    # use a frozenset to get the distinct elements (use frozenset because it is iterable)
    unique_weights = frozenset(weights_list)

    # loop over different weights and insert edges with corresponding width proportional to the weigth
    for el in unique_weights:
        filtered_edges = [e[0:2] for e in G.edges(data=True) if e[2]['weight'] == el] # filter out edges with a certain weight
        Xe = []
        Ye = []
        Ze = []

        # create lists of position of the nodes of filtered edges (add none after every 2 coordinates)
        for e in filtered_edges:
            Xe+=[pos[e[0]][0], pos[e[1]][0], None]
            Ye+=[pos[e[0]][1], pos[e[1]][1], None]
            Ze+=[pos[e[0]][2], pos[e[1]][2], None]

        # create trace with filtered edges (line wwidth = 1.5 * edge weight)
        trace2=go.Scatter3d(x=Xe, y=Ye, z=Ze, mode='lines', name =str(el),
                                line=dict(color='rgb(125,125,125)', width=el*1.5),
                                hoverinfo='text',
                                textposition = 'middle right')
        # add trace to figure
        fig.add_trace(trace2)
        

        # create json from figure
        full_json = plotly.io.to_json(fig)
        # transform json to dict to perform operations on it
        full_dict = json.loads(full_json)
        
        # extact values relative to data and layout keys
        data = json.dumps(full_dict['data'])
        layout = json.dumps(full_dict['layout'])
        
        # concatenate the 2
        graphJSON = data + ',' + layout

    return graphJSON

def generate_json_for_2d_graph():
    
    import pandas as pd
    import networkx as nx
    import json
    from numpyencoder import NumpyEncoder
    
    #import data
    df_edges = pd.read_excel("raan_case_study.xlsx", sheet_name = 0)
    df_nodes = pd.read_excel("raan_case_study.xlsx", sheet_name = 1)
    
    #create graph
    G = nx.DiGraph()
    
    # add nodes and edges
    nodes_list = [(el[0], {'color': el[1], 'label':el[2]}) for _, el in df_nodes.T.items()]
    G.add_nodes_from(nodes_list)
    edges_list = [(el[0], el[1], el[2]) for _, el in df_edges.T.items()]
    G.add_weighted_edges_from(edges_list)
    
    # create list of edges and edges used to create json file
    nodes_list = [{'id': str(el[0]), 'label': el[1]['label'], 'color': el[1]['color']} for el in G.nodes(data=True)]
    edge_list = [{'source': str(el[0]), 'target': str(el[1]), 'value': el[2]['weight'] , 'type': 'standard'} for el in G.edges(data=True)]
    data = {'nodes': nodes_list, 'links': edge_list}
    
    # create json
    
        
    json_file = json.dumps(data, indent=4, sort_keys=True,
              separators=(', ', ': '), ensure_ascii=False,
              cls=NumpyEncoder)
    
    return json_file
        
    