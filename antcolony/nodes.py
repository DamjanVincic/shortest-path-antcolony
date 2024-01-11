import networkx as nx
from .node import Node


class Nodes:
    def __init__(self, filename):
        self.graph = self._load_graph(filename)

    def _load_graph(self, filename):
        graph = nx.Graph()
        nodes = {}
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                node_id = line.split('(')[0]
                coordinates = line.split('(')[1].split(')')[0].split(',')
                nodes[node_id] = {'x': float(coordinates[0]), 'y': float(coordinates[1])}
                graph.add_node(node_id, data=Node(float(coordinates[0]), float(coordinates[1])))

        for line in lines:
            node_id = line.split('(')[0]
            if len(line.split(':')) < 2:
                continue
            incident_nodes = line.split(':')[1].split(",")
            for incident_node in incident_nodes:
                incident_node = incident_node.strip()
                graph.add_edge(node_id, incident_node, distance=graph.nodes[node_id]['data'].distance(graph.nodes[incident_node]['data']))
        return graph

    def __str__(self):
        return str(self.graph.nodes)
