import math
from .ant import Ant


class AntColonyOptimization:
    def __init__(self, nodes, m, alpha, beta, rho, iterations) -> None:
        self.nodes = nodes
        self.m = m  # Number of ants
        self.alpha = alpha  # Influence of pheromones on choice of the next node
        self.beta = beta  # Influence of distance on choice of the next node
        self.rho = rho  # Pheromone evaporation coefficient
        self.iterations = iterations  # Number of iterations

    def send_ants(self, source, destination):
        ants = [Ant(self.nodes, source, destination, self.alpha, self.beta) for _ in range(self.m)]  # Starting ants
        arrived_ants = []  # Ants that arrived to the destination
        moved = True  # Flag to check if any ant has moved, if not, we stop the iteration
        while moved:
            moved = False
            for ant in ants:
                if ant.can_move:
                    ant.move()
                    moved = True
                    if ant.reached_destination:
                        arrived_ants.append(ant)

        self.nodes.evaporate(self.rho)
        self.leave_pheromones(arrived_ants)

        # Choose the ant that found the shortest path to the distance
        best_ant = min(arrived_ants, key=lambda x: x.path_length) if arrived_ants else None
        if best_ant:
            return best_ant.path_length, best_ant.path
        return None

    def leave_pheromones(self, ants):
        # The shortest path found that will be used for the amount of pheromones added
        shortest_path_length = min(ant.path_length for ant in ants) if ants else math.inf
        for ant in ants:
            ant.add_pheromones(shortest_path_length)

    def find_shortest_path(self, source, destination):
        optimum = None

        for i in range(self.iterations):
            current_optimum = self.send_ants(source, destination)
            if not optimum:
                optimum = current_optimum
                continue
            if current_optimum and current_optimum[0] < optimum[0]:
                optimum = current_optimum

        return optimum
    