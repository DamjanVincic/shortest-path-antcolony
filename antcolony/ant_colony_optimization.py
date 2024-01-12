import math
from .ant import Ant


class AntColonyOptimization:
    def __init__(self, nodes, m, alpha, beta, rho, iterations, epsilon) -> None:
        self.nodes = nodes
        self.m = m  # number of ants
        self.alpha = alpha  # influence of pheromones on choice of the next node
        self.beta = beta  # influence of distance on choice of the next node
        self.rho = rho  # pheromone evaporation coefficient
        self.iterations = iterations  # number of iterations
        self.epsilon = epsilon  # maximum difference of path lengths (to stop iterations if we get very similar results)

    def send_ants(self, source, destination):
        ants = [Ant(self.nodes, source, destination, self.alpha, self.beta) for _ in range(self.m)]
        arrived_ants = []
        moved = True
        while moved:
            moved = False
            for ant in ants:
                if not ant.move():
                    if ant.reached_destination:
                        arrived_ants.append(ant)
                else:
                    moved = True
        self.nodes.evaporate(self.rho)
        self.leave_pheromones(arrived_ants)

        best_ant = min(arrived_ants, key=lambda x: x.path_length) if arrived_ants else None
        if best_ant:
            return best_ant.path_length, best_ant.path
        return None

    def leave_pheromones(self, ants):
        shortest_path_length = min(ant.path_length for ant in ants) if ants else math.inf
        for ant in ants:
            ant.add_pheromones(shortest_path_length)

    def find_shortest_path(self, source, destination):
        previous_optimum = None
        for i in range(self.iterations):
            current_optimum = self.send_ants(source, destination)
            if current_optimum and previous_optimum and current_optimum[0] < previous_optimum[0]:
                previous_optimum = current_optimum
            if previous_optimum and abs(previous_optimum[0] - current_optimum[0]) < self.epsilon:
                break
            previous_optimum = current_optimum

        return previous_optimum
    