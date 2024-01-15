from typing import Tuple, List
from .ant import Ant
from .nodes import Nodes


class AntColonyOptimization:
    def __init__(self, nodes: Nodes, m: int, alpha: float, beta: float, rho: float, iterations: int, q: float):
        self.nodes = nodes
        self.m = m  # Number of ants
        self.alpha = alpha  # Influence of pheromones on choice of the next node
        self.beta = beta  # Influence of distance on choice of the next node
        self.rho = rho  # Pheromone evaporation coefficient
        self.iterations = iterations  # Number of iterations
        self.q = q  # The amount of pheromones left on the path by the ant

    def _send_ants(self, source: str, destination: str) -> Tuple[float, List[str]] | None:
        ants = [Ant(self.nodes, source, destination, self.alpha, self.beta, self.q) for _ in range(self.m)]  # Starting ants
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
        self._leave_pheromones(arrived_ants)

        # Choose the ant that found the shortest path to the distance
        best_ant = min(arrived_ants, key=lambda x: x.path_length) if arrived_ants else None
        if best_ant:
            return best_ant.path_length, best_ant.path
        return None

    def _leave_pheromones(self, ants: List[Ant]):
        if len(ants)==0:
            return
        shortest_path=min([ant.path_length for ant in ants])
        for ant in ants:
            ant.add_pheromones(shortest_path)

    def find_shortest_path(self, source: str, destination: str) -> Tuple[float, List[str]] | None:
        optimum = None

        for i in range(self.iterations):
            current_optimum = self._send_ants(source, destination)
            if not optimum:
                optimum = current_optimum
                continue
            if current_optimum and current_optimum[0] < optimum[0]:
                optimum = current_optimum

        return optimum
    