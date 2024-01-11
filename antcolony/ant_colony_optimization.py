from ant import Ant

class AntColonyOptimization:
    def __init__(self,nodes,m,alpha,beta,rho,itetations) -> None:
        self.nodes=nodes
        self.m=m
        self.alpha=alpha
        self.beta=beta
        self.rho=rho
        self.iterations=itetations
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
        self.leave_pheromones(arrived_ants)
        self.nodes.evaporate()

    def leave_pheromones(self,ants):
        shortest_path_length=min(ant.path_length for ant in ants)
        for ant in ants():
            ant.add_pheromones(shortest_path_length)
            

    def find_shortest_path(self,source,destination):
        for i in self.iterations:
            self.send_ants(source,destination)


    