import networkx as nx
import re
from .node import Node


class Nodes:
    def __init__(self, filename, evaporation_rate):
        self._graph = self._load_graph(filename)
        self._evaporation_rate = evaporation_rate

    def _load_graph(self, filename):
        graph = nx.Graph()

        r"""
        (\d+) - capturing group for multiple digits
        \( - the '(' character
        (\d.+) - capturing group for multiple digits and other characters (in our case '.' for float numbers)
        , - the ',' character
        \) - the ')' character
        (?::(.+))? - a non capturing group of a character ':' and a capturing group of any characters (for neighbour IDs)
        """
        pattern = re.compile(r'(\d+)\((\d.+),(\d.+)\)(?::(.+))?')
        with open(filename, 'r') as f:
            for line in f.readlines():
                match = pattern.match(line)
                node_id = match.group(1)
                if not graph.has_node(node_id):
                    graph.add_node(node_id, data=Node(float(match.group(2)), float(match.group(3))))
                elif not graph.nodes[node_id].get('data', None):
                    # if node is in the graph but without its coordinates (if it was added as a neighbour to another one)
                    graph.nodes[node_id]['data'] = Node(float(match.group(2)), float(match.group(3)))

                adjacent_nodes = match.group(4)
                if not adjacent_nodes:
                    continue

                for adjacent_node_id in adjacent_nodes.split(','):
                    if not graph.has_node(adjacent_node_id):
                        graph.add_node(adjacent_node_id)

                    # If there isn't an edge between the node and the neighbour, and the neighbour has coordinates
                    if not graph.has_edge(node_id, adjacent_node_id) and graph.nodes[adjacent_node_id].get('data', None):
                        graph.add_edge(node_id, adjacent_node_id, distance=graph.nodes[node_id]['data'].distance(graph.nodes[adjacent_node_id]['data']), pheromones=1.0)
        return graph

    def get_neighbours(self, node_id):
        try:
            return self._graph.neighbors(node_id)
        except KeyError:
            return None

    def add_pheromones(self, node1, node2, pheromones):
        edge = self[node1, node2]
        edge['pheromones'] += pheromones

    def evaporate(self,rho):
        for edge in self._graph.edges:
            edge['pheromones']*=1-rho

    def __getitem__(self, keys):
        try:
            if isinstance(keys, str):
                return self._graph.nodes[keys]['data']
            elif isinstance(keys, tuple):
                return self._graph.get_edge_data(*keys)
            return None
        except KeyError:
            return None

    def __str__(self):
        return str(self._graph.nodes)
