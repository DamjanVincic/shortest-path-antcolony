import antcolony.utils as utils


class Ant:
    def __init__(self, nodes, source, destination, alpha, beta):
        self.nodes = nodes  # Node representation
        self.current_node = source  # The current node that the ant is on
        self.destination = destination  # The node that the ant wants to get to (food)
        self.alpha = alpha  # Influence of pheromones on choice of the next node
        self.beta = beta  # Influence of distance on choice of the next node

        self.path = [source]  # Path that the ant walked on
        self.path_length = 0  # The length of the path
        self.reached_destination = False  # Flag to check if ant reached the destination
        self.can_move = True  # Flag to check if the ant can move further

    def move(self):
        next_node = self._choose_node()
        if not next_node:
            self.can_move = False
            return

        self.path.append(next_node)
        self.path_length += self.nodes[self.current_node, next_node]['distance']
        self.current_node = next_node

        if self.current_node == self.destination:
            self.reached_destination = True
            self.can_move = False

    def _choose_node(self):
        unvisited_neighbours = self._get_unvisited_neighbours()
        if len(unvisited_neighbours) == 0:
            return None

        edge_coefficients = {}  # Edge coefficients (desirability)
        for neighbour in unvisited_neighbours:
            edge = self.nodes[self.current_node, neighbour]
            if edge['distance'] == 0:  # Some nodes have the same coordinates
                continue
            edge_coefficients[neighbour] = utils.edge_coefficient(edge['pheromones'], edge['distance'], self.alpha, self.beta)

        # Get the next node by the roulette selection method
        next_node = utils.roulette_selection(edge_coefficients)
        return next_node

    def _get_unvisited_neighbours(self):
        # Get the nodes that the ant hasn't visited yet
        return [node for node in self.nodes.get_neighbours(self.current_node) if node not in self.path]

    def add_pheromones(self, shortest_path_length):
        # Deposit pheromones on the path from source to destination based on the shortest path length
        for i in range(len(self.path) - 1, 0, -1):
            self.nodes.add_pheromones(self.path[i], self.path[i-1], shortest_path_length/self.path_length)
