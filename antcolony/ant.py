from .nodes import Nodes
import utils


class Ant:
    def __init__(self, nodes, source, destination, alpha, beta):
        self.nodes = nodes
        self.current_node = source
        self.destination = destination
        self.alpha = alpha
        self.beta = beta
        self.path = [source]
        self.path_length = 0
        self.visited_nodes = set(source)

    def _choose_node(self):
        unvisited_neighbours = self._get_unvisited_neighbours()
        if len(unvisited_neighbours) == 0:
            return None

        edge_coefficients = {}
        for neighbour in unvisited_neighbours[0]:
            edge = self.nodes[self.current_node, neighbour]
            edge_coefficients[neighbour] = utils.edge_coefficient(edge['pheromones'], edge['distance'], self.alpha, self.beta)

        next_node = utils.roulette_selection(edge_coefficients)
        return next_node

    def _get_unvisited_neighbours(self):
        return [node for node in self.nodes.get_neighbours(self.current_node) if node not in self.visited_nodes]

