import math

def edge_probability(pheromones,distance,alpha,beta):
    return math.pow(pheromones,alpha)*math.pow(1/distance,beta)