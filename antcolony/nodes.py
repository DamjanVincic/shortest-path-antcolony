import networkx as nx
import re
from .node import Node


class Nodes:
    def __init__(self, filename):
        self.graph = self._load_graph(filename)

    def _load_graph(self, filename):
        graph = nx.Graph()
        pattern = re.compile(r'(\d+)\((\d.+),(\d.+)\)(?::(.+))?')
        with open(filename, 'r') as f:
            for line in f.readlines():
                match = pattern.match(line)
                node_id = match.group(1)
                if not graph.has_node(node_id):
                    graph.add_node(node_id, data=Node(float(match.group(2)), float(match.group(3))))
                elif not graph.nodes[node_id].get('data', None):
                    graph.nodes[node_id]['data'] = Node(float(match.group(2)), float(match.group(3)))

                adjacent_nodes = match.group(4)
                if not adjacent_nodes:
                    continue

                for adjacent_node_id in adjacent_nodes.split(','):
                    if not graph.has_node(adjacent_node_id):
                        graph.add_node(adjacent_node_id)
                    if not graph.has_edge(node_id, adjacent_node_id) and graph.nodes[adjacent_node_id].get('data', None):
                        graph.add_edge(node_id, adjacent_node_id, distance=graph.nodes[node_id]['data'].distance(graph.nodes[adjacent_node_id]['data']))
        return graph

    def __str__(self):
        return str(self.graph.nodes)
