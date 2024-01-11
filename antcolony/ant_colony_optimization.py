from .ant import Ant
import math

class AntColonyOptimization:
    def __init__(self,nodes,m,alpha,beta,rho,itetations, epsilon) -> None:
        self.nodes=nodes
        self.m=m
        self.alpha=alpha
        self.beta=beta
        self.rho=rho
        self.iterations=itetations
        self.epsilon=epsilon
    """
        m - number of ants
        alpha - influence of pheromones on choice next node
        beta - influence of distance on choice of next node
        rho - speed of pheromone evaporation
        source - first node of the path
        destination -
        iterations - max number of iterations
    """
    def send_ants(self,source,destination):
        ants=[Ant(self.nodes,source,destination,self.alpha,self.beta)for _ in range(self.m)]
        arrived_ants=[]
        while len(ants)!=0:
            for ant in ants:
                if not ant.move():
                    ants.remove(ant)
                    if ant.reached_destination:
                        arrived_ants.append(ant)
        self.nodes.evaporate(self.rho)
        self.leave_pheromones(arrived_ants)

        best_ant = min(ants, key=lambda x: x.path_length) if ants else None
        if best_ant:
            return best_ant.path_length, best_ant.path
        return None

    def leave_pheromones(self,ants):
        shortest_path_length=min(ant.path_length for ant in ants) if ants else math.inf
        for ant in ants:
            ant.add_pheromones(shortest_path_length)

    def find_shortest_path(self,source,destination):
        previous_optimum = None
        for i in range(self.iterations):
            current_optimum = self.send_ants(source,destination)
            if current_optimum and current_optimum[0] < previous_optimum[0]:
                previous_optimum = current_optimum
            if previous_optimum and abs(previous_optimum[0] - current_optimum[0]) < self.epsilon:
                break

        return previous_optimum
    