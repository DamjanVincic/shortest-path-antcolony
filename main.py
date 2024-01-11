import networkx as nx
import math
import matplotlib.pyplot as plt

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def load_graph():
    graph=nx.Graph()
    with open("data_path_nodes.txt",'r') as f:
        nodes = {}
        lines = f.readlines()
        for line in lines:
            node_id=line.split('(')[0]
            coordinates=line.split('(')[1].split(')')[0].split(',')
            x=float(coordinates[0])
            y=float(coordinates[1])
            nodes[node_id]={}
            nodes[node_id]['x']=x
            nodes[node_id]['y']=y
            graph.add_node(node_id)
    for line in lines:
        node_id=line.split('(')[0]
        if len(line.split(':'))<2:
            continue
        incident_nodes=line.split(':')[1].split(",")
        for incident_node in incident_nodes:
            incident_node=incident_node.strip()
            graph.add_edge(node_id,incident_node,weight=distance(nodes[node_id]['x'],nodes[node_id]['y'],nodes[incident_node]['x'],nodes[incident_node]['y']))
    return graph


if __name__ == "__main__":
    g=load_graph()
    nx.draw(g)
    plt.show()
