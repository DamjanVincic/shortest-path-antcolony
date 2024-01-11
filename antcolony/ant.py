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
        self.reached_destination = False

    def move(self):
        next_node = self._choose_node()
        if not next_node or self.reached_destination:
            return False

        self.path.append(next_node)
        self.visited_nodes.add(next_node)
        self.path_length += self.nodes[self.current_node, next_node]
        self.current_node = next_node

        if self.current_node == self.destination:
            self.reached_destination = True

        return True

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

    def add_pheromones(self, shortest_path_length):
        for i in range(len(self.path) - 1, 0, -1):
            self.nodes.add_pheromones(self, self.path[i], self.path[i-1], shortest_path_length/self.path_length)
