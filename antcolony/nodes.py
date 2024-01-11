import networkx as nx
import math


class Nodes:
    def __init__(self, filename):
        self.graph = self._load_graph(filename)

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def _load_graph(self, filename):
        graph = nx.Graph()
        nodes = {}
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                node_id = line.split('(')[0]
                coordinates = line.split('(')[1].split(')')[0].split(',')
                nodes[node_id] = {'x': float(coordinates[0]), 'y': float(coordinates[1])}
                graph.add_node(node_id)

        for line in lines:
            node_id = line.split('(')[0]
            if len(line.split(':')) < 2:
                continue
            incident_nodes = line.split(':')[1].split(",")
            for incident_node in incident_nodes:
                incident_node = incident_node.strip()
                graph.add_edge(node_id, incident_node,
                               weight=self.distance(nodes[node_id]['x'], nodes[node_id]['y'], nodes[incident_node]['x'],
                                                    nodes[incident_node]['y']))
        return graph

    def __str__(self):
        return str(self.graph.nodes)
